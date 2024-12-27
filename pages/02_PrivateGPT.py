import time
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import TextLoader, PyPDFLoader, UnstructuredFileLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter
from langchain.embeddings import OllamaEmbeddings, CacheBackedEmbeddings
# from langchain.vectorstores import Chroma, FAISS
from langchain_community.vectorstores import FAISS, Chroma
from langchain.storage import LocalFileStore
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough, RunnableLambda
# from langchain.chat_models import ChatOllama
from langchain_ollama import ChatOllama
from langchain.callbacks.base import BaseCallbackHandler

st.set_page_config(
    page_title="PrivateGPT",
    page_icon="📃",
)

class ChatCallbackHandler(BaseCallbackHandler):
    message = ""
    
    # For diverse argumnets, * and ** used
    def on_llm_start(self, *args, **kwargs):
        self.message_box = st.empty()

    def on_llm_end(self, *args, **kwargs):
        save_message(self.message, 'ai')

    def on_llm_new_token(self, token, *args, **kwargs):
        self.message += token
        self.message_box.markdown(self.message)


# streaming argument 
llm = ChatOllama(
    model = 'mistral:latest',
    temperature = 0.1,
    streaming=True,
    callbacks=[
        ChatCallbackHandler()
    ]
)

@st.cache_data(show_spinner='Embedding file....')
def embed_file(file):
    file_content = file.read()
    file_path = f'./.cache/private_files/{file.name}'
    with open(file_path, 'wb') as f:
        f.write(file_content)

    cache_dir = LocalFileStore(f"./.cache/private_embeddings/{file.name}")
    splitter = CharacterTextSplitter(
        separator = '\n',
        chunk_size = 600,
        chunk_overlap= 50,
    )

    # 해당 loader는 pdf, txt, docx와 모두 호환됩니다.
    # 여기가 특화 데이터셋입니다. 추후에 변경을 하면 됩니다. 
    loader = UnstructuredFileLoader(file_path)
    docs = loader.load_and_split(text_splitter=splitter)
    embeddings = OllamaEmbeddings(
        model = 'mistral:latest'
    )
    cached_embeddings = CacheBackedEmbeddings.from_bytes_store(
        embeddings, cache_dir
    )
    vectorstore = FAISS.from_documents(docs, cached_embeddings)
    retriever = vectorstore.as_retriever()
    return retriever

def save_message(message, role):
    st.session_state['messages'].append({'message':message,'role':role})

def send_message(message, role, save=True):
    with st.chat_message(role):
        st.markdown(message)
    if save:
        save_message(message, role)

def format_docs(docs):
    return "\n\n".join(document.page_content for document in docs)

def paint_history():
    for message in st.session_state['messages']:
        send_message(message['message'], message['role'], save=False)

prompt = ChatPromptTemplate.from_messages([
    ('system',
    '''
    Answer the question using ONLY the following context. If you don't know the answer just say you don't know. Don't make anything up
    
    Context: {context}
    '''),
    ('human', '{question}')
])

st.title("DocumentGPT")

st.markdown('''
Welcome!

Use this chatbot to ask questions to an AI about your files!

Upload your file on the side bar
''')

with st.sidebar:
    file = st.file_uploader('Upload a .txt .pdf or .docx file', type = ['pdf','txt','docx'])

if file:
    retriever = embed_file(file) 
    send_message('I"m ready! Ask away', 'ai', save=False)
    paint_history()
    message = st.chat_input('Ask anything about your file...')
    if message:
        send_message(message, 'human')
        chain = {
            'context':retriever | RunnableLambda(format_docs),
            'question' : RunnablePassthrough()
        } | prompt | llm 
        with st.chat_message('ai'):
            chain.invoke(message)
        # send_message(response.content, 'ai')
        
else:
    st.session_state['messages'] = []
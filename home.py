import streamlit as st
from datetime import datetime
st.set_page_config(
    page_title='FullstackGPT',
    page_icon = '※',
)
today = datetime.today().strftime("%H:%M:%S")
st.write(today)

st.title("FullstackGPT Home")

with st.sidebar:
    st.sidebar.title('sidebar title')
    name = st.sidebar.text_input('sidebar_input')
    st.write(name)

st.subheader("Welcome to Streamlit!")
tab_one, tab_two, tab_three = st.tabs(['A','B', 'C'])
with tab_one:
    st.write('a')

with tab_two:
    st.write('b')
    
with tab_three:
    st.write('c')

st.markdown(
    '''
    Welcome to my FullstackGPT Portfolio!

    Here are the apps I made:

    - [x] [DocumentGPT](/DocumentGPT)
    - [x] [PrivateGPT](/PrivateGPT)
    - [x] [QuizGPT](/QuizGPT)
    - [ ] [SiteGPT](/SiteGPT)
    - [ ] [MeetingGPT](/MeetingGPT)
    - [ ] [InvestorGPT](/InvestorGPT)
    '''
)
st.write("streamlit is ui tool using python")
name = st.text_input("What is your name?")
st.write(name)

model = st.selectbox('Choose your model', ('GPT-3','GPT-4'))
if model == 'GPT-3':
    value = st.slider(
        'temperature',
        min_value=0.1,
        max_value=1.0
        )
    st.write(value)
else: 
    st.write("You can't use GPT-4")
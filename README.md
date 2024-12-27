# 프로젝트명: Langchain and Rag Toy Project

## 1. 개발 환경

- Python 3.9.20

- 그 외 라이브러리는 requirements.txt 파일을 참조하세요.

## 2. 레포지토리 개요

- 이 레포지토리는 LangChain 라이브러리를 활용하여 다양한 RAG(Retrieval-Augmented Generation)를 구현한 Toy Project입니다.

- 추후 RAG를 활용한 프로젝트를 진행할 때 참고하기 위해 기록한 프로젝트로, 다음과 같은 주요 작업이 포함되어 있습니다:

## 3. 주요 작업 내역

- 2024-12-10: DocumentGPT 완성 (특정 데이터셋을 검색하여 답변하는 서비스)

## 4. 사용 방법

- 필요한 의존성을 설치합니다:

```bash
pip install -r requirements.txt
```
- Streamlit을 실행하여 서비스를 실행합니다:
```bash
streamlit run home.py
```

## 5. 개발 내용

### Document GPT

법률. 의학 등 어려운 용어로 가득한 각종 문서. AI로 빠르게 파악하고 싶다면?

AI로 신속하고 정확하게 문서 내용을 파악하고 정리한 뒤, 필요한 부분만 쏙쏙 골라내어 사용하세요. DocumentGPT 챗봇을 사용하면, AI가 문서(.txt, .pdf, .docx 등)를 꼼꼼하게 읽고, 해당 문서에 관한 질문에 척척 답변해 줍니다.

### Private GPT

회사 기밀이 유출될까 걱정된다면? 이제 나만이 볼 수 있는 비공개 GPT를 만들어 활용하세요!

DocumentGPT와 비슷하지만 로컬 언어 모델을 사용해 비공개 데이터를 다루기에 적합한 챗봇입니다. 데이터는 컴퓨터에 보관되므로 오프라인에서도 사용할 수 있습니다. 유출 걱정 없이 필요한 데이터를 PrivateGPT에 맡기고 업무 생산성을 높일 수 있어요.
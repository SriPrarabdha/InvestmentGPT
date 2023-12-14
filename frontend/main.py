import os

import streamlit as st
from streamlit_chat import message
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.vectorstores import faiss
from langchain.text_splitter import RecursiveCharacterTextSplitter
import tempfile

import pandas as pd
import dotenv

dotenv.load_dotenv()

assert os.environ.get("OPENAI_API_KEY")

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size = 100,
    chunk_overlap  = 20,
    length_function = len,
    is_separator_regex = False,
)

st.title('InvestmentGPT 🤖')
st.write("Hello, 👋 I am Your AI Assistant and I am here to guide you with your investment journey")

user_api_key = st.sidebar.text_input(
    label="#### Your OpenAI API key 👇",
    placeholder="Paste your openAI API key, sk-",
    type="password")

uploaded_file = st.sidebar.file_uploader("upload", type="csv")

if uploaded_file :
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_file_path = tmp_file.name

    loader = CSVLoader(file_path=tmp_file_path, encoding="utf-8")
    data = loader.load()

    chunks = text_splitter.create_documents(data)

    embeddings = OpenAIEmbeddings()
    vectors = faiss.FAISS.from_documents(chunks, embeddings)

    chain = ConversationalRetrievalChain.from_llm(llm = ChatOpenAI(temperature=0.0,model_name='gpt-3.5-turbo', openai_api_key=user_api_key),
                                                                      retriever=vectors.as_retriever())

    def conversational_chat(query):
        
        result = chain({"question": query, "chat_history": st.session_state['history']})
        st.session_state['history'].append((query, result["answer"]))
        
        return result["answer"]
    
    if 'history' not in st.session_state:
        st.session_state['history'] = []

    if 'generated' not in st.session_state:
        st.session_state['generated'] = ["Hello ! Ask me anything about " + uploaded_file.name + " 🤗"]

    if 'past' not in st.session_state:
        st.session_state['past'] = ["Hey ! 👋"]
        
    #container for the chat history
    response_container = st.container()
    #container for the user's text input
    container = st.container()

    with container:
        with st.form(key='my_form', clear_on_submit=True):
            
            user_input = st.text_input("Query:", placeholder="Talk about your csv data here (:", key='input')
            submit_button = st.form_submit_button(label='Send')
            
        if submit_button and user_input:
            output = conversational_chat(user_input)
            
            st.session_state['past'].append(user_input)
            st.session_state['generated'].append(output)

    if st.session_state['generated']:
        with response_container:
            for i in range(len(st.session_state['generated'])):
                message(st.session_state["past"][i], is_user=True, key=str(i) + '_user', avatar_style="big-smile")
                message(st.session_state["generated"][i], key=str(i), avatar_style="thumbs")

# with st.sidebar:
#     st.write('*Your Investment Journey begins here.*')

#     with st.expander("What's the LLM Doing"):
#         if user_csv is None:
#             st.write("First start your conversation!!")
#         # else:
#         #     st.write(llm("What are the steps of EDA"))
#         # messages.append(HumanMessage(content="What are the steps of EDA"),)
#         # st.write(llm.invoke(messages).content)
        


# if 'clicked' not in st.session_state:
#     st.session_state.clicked = {1:False}

# def clicked(button):
#     st.session_state.clicked[button] = True

# st.button("Let's get Started", on_click=clicked, args=[1])

# if st.session_state.clicked[1]:
#     st.header("Start with uploading a file or just start Questions")

#     user_csv = st.file_uploader("Upload Your File Here" , type="csv")

#     if user_csv is not None:
#         user_csv.seek(0)
#         df = pd.read_csv(user_csv, low_memory=False)

#         pandas_agent = create_pandas_dataframe_agent(OpenAI(temperature=0), df)

#         question = "which columns are present in this data , alos provide the mean of the values for the first column"

#         answer = pandas_agent.run(question)

#         st.write(answer)

    


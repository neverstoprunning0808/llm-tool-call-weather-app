import streamlit as st
from utils import perform_rag
import os 
from dotenv import load_dotenv
from groq import Groq


st.title("Weather RAG Chat App")


@st.cache_resource
def get_client():
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        api_key = st.secrets.get("GROQ_API_KEY")
    return Groq(api_key=api_key)

client = get_client()

if "messages" not in st.session_state:
    st.session_state.messages = []
    
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

if prompt := st.chat_input("Ask a question"):
    st.session_state.messages.append({'role': 'user', 'content': prompt})
    with st.chat_message('user'):
        st.markdown(prompt)

    response = perform_rag(client, prompt)
    st.session_state.messages.append({'role': 'assistant', 'content': response})

    with st.chat_message('assistant'):
        st.markdown(response)
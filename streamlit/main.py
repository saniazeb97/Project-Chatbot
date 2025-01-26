import streamlit as st
from .api_client import upload_pdf_to_backend
from .ui_helpers import display_chat_history, ask_question

st.title("CHAT WITH PDF")
uploaded_file = st.sidebar.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    response = upload_pdf_to_backend(uploaded_file)
    if response.get("status") == "success":
        embedding_path = response.get("embedding_file_path")
        st.sidebar.success("Embeddings created!")
    else:
        st.sidebar.error(response.get("message"))

display_chat_history()
ask_question()

import streamlit as st

def display_chat_history():
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    for question, answer in st.session_state.chat_history:
        st.write(f"**You:** {question}")
        st.write(f"**Answer:** {answer}")
        st.write("---")

def ask_question():
    user_input = st.text_input("Ask a question about the document:")
    if user_input:
        # Add chat retrieval and response logic here
        st.session_state.chat_history.append((user_input, "Mock response"))

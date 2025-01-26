import streamlit as st
from api_client import upload_pdf_to_backend
from ui_helpers import display_chat_history, ask_question
from langchain.chains import SequentialChain, TransformChain, ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_community.llms import Ollama

# Initialize session state variables
if "retriever" not in st.session_state:
    st.session_state.retriever = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

llm = Ollama(model="llama2")

# File upload logic
uploaded_file = st.sidebar.file_uploader("Upload a PDF", type=["pdf"])
if uploaded_file:
    response = upload_pdf_to_backend(uploaded_file)

    # Debugging: Log the response from the backend
    st.write(f"Backend response: {response}")

    # Check if the response is valid
    if response.get("status") == "success":
        embedding_path = response.get("embedding_file_path")
        if embedding_path:
            st.session_state.retriever = embedding_path  # Save retriever for later use
            st.sidebar.success("Embeddings created!")
        else:
            st.sidebar.error("Failed to retrieve valid embedding path.")
    else:
        st.sidebar.error(response.get("message"))

# Debugging: Check session state for retriever
st.write(f"Session State - Retriever: {st.session_state.retriever}")

# Proceed only if embeddings are available
if st.session_state.retriever:
    # Display chat history
    display_chat_history()

    # User input field
    user_input = st.text_input("Ask a question about the document:", "")

    if user_input:
        # Check the user input
        st.write(f"User input: {user_input}")

        # Check if question is not a duplicate
        if user_input not in [q for q, _ in st.session_state.chat_history]:
            # Conversational Retrieval Chain
            conversational_retrieval = ConversationalRetrievalChain.from_llm(
                llm=llm,
                retriever=st.session_state.retriever
            )

            # Memory for conversation context
            memory = ConversationBufferMemory(return_messages=True)

            # Transform Chain to handle input transformation
            transform = TransformChain(
                input_variables=["input"],
                output_variables=["question", "chat_history"],
                transform=lambda inputs: {
                    "question": inputs["input"],
                    "chat_history": st.session_state.chat_history,
                },
            )

            # Combine everything into a Sequential Chain
            chat = SequentialChain(
                memory=memory,
                input_variables=["input"],
                output_variables=["answer"],
                chains=[transform, conversational_retrieval],
            )

            # Run the chat model
            with st.spinner("Thinking..."):
                response = chat.run({"input": user_input})

                # Store the question and answer in session state to keep history
                st.session_state.chat_history.append((user_input, response))

                # Automatically reset the input box by rerunning the app
                st.experimental_rerun()  # Re-run the script to reset the input box

                # Display the new answer (this will show after rerun)
                st.write("### Answer")
                st.write(response)

else:
    st.write("### Please upload a PDF to start the conversation.")

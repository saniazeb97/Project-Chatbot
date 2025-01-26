import os
import shutil
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

# Define directories
UPLOAD_DIR = "temp_documents"
EMBEDDINGS_DIR = "embeddings_store"

async def process_pdf(file):
    # Ensure directories exist
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)
    
    if not os.path.exists(EMBEDDINGS_DIR):
        os.makedirs(EMBEDDINGS_DIR)
    
    # Save the uploaded PDF file to the temp_documents folder
    temp_file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(temp_file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    try:
        # Load the PDF using PyPDFLoader
        loader = PyPDFLoader(temp_file_path)
        documents = loader.load()

        # Split the document text into chunks
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=100)
        splits = text_splitter.split_documents(documents)

        # Create embeddings using OllamaEmbeddings
        embeddings = OllamaEmbeddings()
        db = FAISS.from_documents(splits, embeddings)

        # Save the embeddings locally
        embedding_file_path = os.path.join(EMBEDDINGS_DIR, f"{file.filename}.faiss")
        db.save_local(embedding_file_path)

        return {
            "status": "success",
            "message": "PDF processed successfully!",
            "embedding_file_path": embedding_file_path,
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

import os
import shutil
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

UPLOAD_DIR = "temp_documents"
EMBEDDINGS_DIR = "embeddings_store"

async def process_pdf(file):
    # Save the uploaded PDF
    temp_file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(temp_file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    try:
        loader = PyPDFLoader(temp_file_path)
        documents = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=100)
        splits = text_splitter.split_documents(documents)

        embeddings = OllamaEmbeddings()
        db = FAISS.from_documents(splits, embeddings)

        embedding_file_path = os.path.join(EMBEDDINGS_DIR, f"{file.filename}.faiss")
        db.save_local(embedding_file_path)

        return {
            "status": "success",
            "message": "PDF processed successfully!",
            "embedding_file_path": embedding_file_path,
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

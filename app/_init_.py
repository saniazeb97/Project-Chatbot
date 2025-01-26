from fastapi import FastAPI
import os

# Initialize FastAPI app
app = FastAPI()

# Create required directories if they don't exist
UPLOAD_DIR = "temp_documents"
EMBEDDINGS_DIR = "embeddings_store"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(EMBEDDINGS_DIR, exist_ok=True)

# Expose the app for imports
__all__ = ["app", "UPLOAD_DIR", "EMBEDDINGS_DIR"]

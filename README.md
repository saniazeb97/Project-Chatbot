# Chatbot Application

This project provides a chatbot application with a **FastAPI** backend and a **Streamlit** frontend. The backend serves API endpoints for query processing, while the frontend is responsible for interacting with users and displaying responses. The chatbot can answer questions based on information extracted from uploaded PDFs.

## Features
- **FastAPI** backend for processing and serving chatbot queries.
- **Streamlit** frontend for an interactive user interface.
- PDF document upload and text extraction functionality.
- Integration with Natural Language Processing (NLP) models for answering questions based on document content.
- Deployment-ready with Docker for easy setup and distribution.

## Setup Instructions

### Prerequisites

Before setting up the project, ensure you have the following:
- Python 3.9 or higher.
- Docker (optional, for containerized deployment).
- Git (to clone the repository).

### Step-by-Step Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/saniazeb97/Project-Chatbot.git
   cd <repository>

2. **Install Dependencies**:
    pip install -r requirements.txt

3. **Running the Application**:
    
    ### Start FastAPI Backend:
    uvicorn app.main:app --host 0.0.0.0 --port 8000

    ### Start Streamlit Frontend:
    streamlit run streamlit.main.py


## API Documentation

### `/upload_pdf`

- **Method**: `POST`
- **Description**: Uploads a PDF document to the backend for extraction and processing..
- **Request Body**: Form-data with a key file (file input).

```Response
{

  "message": "File uploaded successfully."
}



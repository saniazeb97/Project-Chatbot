import requests

UPLOAD_ENDPOINT = "http://127.0.0.1:8000/upload_pdf/"

def upload_pdf_to_backend(uploaded_file):
    try:
        response = requests.post(
            UPLOAD_ENDPOINT,
            files={"file": (uploaded_file.name, uploaded_file, "application/pdf")},
        )
        return response.json()
    except Exception as e:
        return {"status": "error", "message": str(e)}

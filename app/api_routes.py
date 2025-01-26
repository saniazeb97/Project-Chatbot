from fastapi import APIRouter, UploadFile, File
from .services import process_pdf

router = APIRouter()

@router.post("/upload_pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    return await process_pdf(file)

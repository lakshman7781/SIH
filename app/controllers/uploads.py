from fastapi import APIRouter, UploadFile, File, Form
from app.workflows.upload import document_process_workflow
from app.integrations.function_calls import DocumentType
from enum import Enum
import os

router = APIRouter()

@router.get("/upload")
def make_upload():
    return {"message": "This is the upload endpoint"}@router.post("/process_document")

@router.post("/process_document")
async def upload_file(document_type: DocumentType = Form(...), file: UploadFile = File(...)):
    temp_dir = "app/temp"
    file_location = os.path.join(temp_dir, file.filename)
    
    try:
        with open(file_location, "wb") as f:
            f.write(await file.read())
        
        structured_text = await document_process_workflow(file_path=file_location, document_type=document_type)
        
        return {"message": "File uploaded successfully", "result": structured_text}
    
    except Exception as e:
        return {"error": str(e)}
    
    finally:
        if os.path.exists(file_location):
            os.remove(file_location)
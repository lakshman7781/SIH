from fastapi import APIRouter,UploadFile,File
from app.workflows.upload import data_pipeline
import os

router = APIRouter()

@router.get("/upload")
def make_upload():
    return {"message": "This is the upload endpoint"}

#todo: add document type to the request
@router.post("/process_document")
async def upload_file(file: UploadFile = File(...)):
    temp_dir = "app/temp"
    file_location = os.path.join(temp_dir, file.filename)
    with open(file_location, "wb") as f:
        f.write(await file.read())
        
    structured_text = await data_pipeline(file_path=file_location)
    os.remove(file_location)
    return {"message": "File uploaded successfully", "result": structured_text}
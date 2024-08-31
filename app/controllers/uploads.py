from fastapi import APIRouter
from app.workflows.upload import data_pipeline

router = APIRouter()

@router.get("/upload")
def make_upload():
    return {"message": "This is the upload endpoint"}

@router.post("/uploadfile/")
async def upload_file():
    #todo: get the file dynamically
    file_path = "samples/70__ATS_rating.pdf"
    result = await data_pipeline(file_path=file_path)
    return {"message": "File uploaded successfully", "result": result}
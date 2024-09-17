from fastapi import APIRouter, UploadFile, File, Form
from app.workflows.upload import document_process_workflow
from app.integrations.function_calls import DocumentType
from app.integrations.firebase import upload_to_firebase, list_files_from_firebase, download_from_firebase,get_download_url
from fastapi.responses import FileResponse
import os
import json
import logging


router = APIRouter()

@router.get("/upload")
def make_upload():
    return {"message": "This is the upload endpoint"}

@router.post("/process_document")
async def upload_file(document_type: DocumentType = Form(...), file: UploadFile = File(...)):
    temp_dir = "app/temp"
    file_location = os.path.join(temp_dir, file.filename)
    json_filename = f"{os.path.splitext(file.filename)[0]}.json"
    json_file_location = os.path.join(temp_dir, json_filename)
    
    try:
        with open(file_location, "wb") as f:
            f.write(await file.read())
        
        structured_text = await document_process_workflow(file_path=file_location, document_type=document_type)
        
        # Save the result in a JSON file
        with open(json_file_location, "w") as json_file:
            json.dump(structured_text, json_file)

        # Upload the actual file and the JSON file to Firebase
        with open(file_location, "rb") as actual_file, open(json_file_location, "rb") as json_file:
            upload_to_firebase([actual_file, json_file], [file.filename, json_filename])
        
        return {"message": "File uploaded successfully", "result": structured_text}
    
    except Exception as e:
        logging.error(f"Error in processing document: {str(e)}")
        return {"error": str(e)}
    
    finally:
        if os.path.exists(file_location):
            os.remove(file_location)
        if os.path.exists(json_file_location):
            os.remove(json_file_location)
            
@router.get("/get_all")
async def get_all_files():
    directory_path = "Transformo_Docs/"
    file_paths = list_files_from_firebase(directory_path)
    return {"files": file_paths}

@router.get("/download")
async def download_file(storage_path: str):
    # storage_path = "Transformo_Docs/Krishna_vamsi_final/Krishna_vamsi_final.pdf"
    signed_url = get_download_url(storage_path)
    file_path = download_from_firebase(signed_url, storage_path.split('/')[-1])
    return FileResponse(file_path, media_type='application/octet-stream', filename=storage_path.split('/')[-1])

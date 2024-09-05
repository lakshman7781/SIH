from fastapi import APIRouter, UploadFile, File, Form
from app.workflows.upload import document_process_workflow
from app.integrations.function_calls import DocumentType
from app.integrations.firebase import upload_to_firebase
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

        # Upload the JSON file to Firebase
        with open(json_file_location, "rb") as json_file:
            upload_to_firebase(json_file, json_filename)
        
        return {"message": "File uploaded successfully", "result": structured_text}
    
    except Exception as e:
        logging.error(f"Error in processing document: {str(e)}")
        return {"error": str(e)}
    
    finally:
        if os.path.exists(file_location):
            os.remove(file_location)
        if os.path.exists(json_file_location):
            os.remove(json_file_location)
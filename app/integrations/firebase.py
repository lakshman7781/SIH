from firebase_admin import credentials, initialize_app, storage
from fastapi import HTTPException, UploadFile
import mimetypes
import logging
import os 
from datetime import timedelta
import requests


def initialize_firebase_app():
    cred = credentials.Certificate("app/configs/firebase.json")
    initialize_app(cred, {
        'storageBucket': 'portfolio-8ccd0.appspot.com'
    })

def upload_to_firebase(files, filenames):
    try:
        logging.info("Starting upload to Firebase")
        bucket = storage.bucket()
        
        folder_name = os.path.splitext(filenames[0])[0]
        storage_folder_path = f"Transformo_Docs/{folder_name}/"
        
        for file, filename in zip(files, filenames):
            storage_path = f"{storage_folder_path}{filename}"
            blob = bucket.blob(storage_path)
            content_type = mimetypes.guess_type(filename)[0]
            blob.upload_from_file(file, content_type=content_type)
            logging.info(f"File uploaded to Firebase at {storage_path}")
        
        return storage_folder_path
    except Exception as e:
        logging.error(f"Error in uploading file to Firebase Storage: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error in uploading file to Firebase Storage: {str(e)}")

    
def download_from_firebase(url, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        # Ensure the app/temp directory exists
        temp_dir = "app/trash"
        os.makedirs(temp_dir, exist_ok=True)
        
        # Define the file path in the app/temp directory
        file_path = os.path.join(temp_dir, filename)
        
        # Write the content to the file
        with open(file_path, 'wb') as f:
            f.write(response.content)
        
        logging.info(f"File downloaded to {file_path}")
        return file_path
    except Exception as e:
        logging.error(f"Error in downloading file from Firebase Storage: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error in downloading file from Firebase Storage: {str(e)}")
    
def delete_document_from_firebase(document_url):
    try:
        bucket = storage.bucket()
        blob = bucket.blob(document_url)
        blob.delete()
        print(
            f"Document {document_url} deleted successfully from Firebase Storage.")
    except Exception as e:
        print(f"Error deleting document from Firebase Storage: {e}")
        
def get_download_url(storage_path: str):
    try:
        bucket = storage.bucket()
        blob = bucket.blob(storage_path)
        url = blob.generate_signed_url(expiration=300, version="v4", method="GET")
        return url
    except:
        raise HTTPException(status_code=500, detail="Error in getting download url from Firebase Storage.")  
      
def list_files_from_firebase(directory_path):
    try:
        logging.info(f"Listing files from Firebase directory: {directory_path}")
        bucket = storage.bucket()
        blobs = bucket.list_blobs(prefix=directory_path)
        
        file_info = []
        for blob in blobs:
            if not blob.name.endswith('/'):
                signed_url = blob.generate_signed_url(
                    version="v4",
                    expiration=timedelta(hours=1),
                    method="GET"
                )
                file_info.append({"name": blob.name, "signed_url": signed_url})
        
        logging.info(f"Files found in directory {directory_path}: {file_info}")
        return file_info
    except Exception as e:
        logging.error(f"Error in listing files from Firebase Storage: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error in listing files from Firebase Storage: {str(e)}")
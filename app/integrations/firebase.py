from firebase_admin import credentials, initialize_app, storage
from fastapi import HTTPException, UploadFile
import mimetypes
import logging

def initialize_firebase_app():
    cred = credentials.Certificate("app/configs/firebase.json")
    initialize_app(cred, {
        'storageBucket': 'portfolio-8ccd0.appspot.com'
    })

def upload_to_firebase(file, filename):
    try:
        logging.info("Starting upload to Firebase")
        # Upload file to Firebase Storage
        bucket = storage.bucket()
        storage_path = f"Transformo_Docs/{filename}"
        blob = bucket.blob(storage_path)
        content_type = mimetypes.guess_type(filename)[0]
        blob.upload_from_file(file, content_type=content_type)
        logging.info(f"File uploaded to Firebase at {storage_path}")
        return storage_path
    except Exception as e:
        logging.error(f"Error in uploading file to Firebase Storage: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error in uploading file to Firebase Storage: {str(e)}")

    
async def download_from_firebase(storage_path: str):
    try:
        # Download file from Firebase Storage
        bucket = storage.bucket()
        blob = bucket.blob(storage_path)
        file_path = "app/temp/" + storage_path.split('/')[-1]
        blob.download_to_filename(file_path)
        return file_path
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error in downloading file from Firebase Storage.")    
    
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
        # Get download url for file from Firebase Storage
        bucket = storage.bucket()
        blob = bucket.blob(storage_path)
        url = blob.generate_signed_url(expiration=300, version="v4", method="GET")
        return url
    except:
        raise HTTPException(status_code=500, detail="Error in getting download url from Firebase Storage.")        
from firebase_admin import credentials, initialize_app, storage

from fastapi import HTTPException, UploadFile
import mimetypes

def initialize_firebase_app():
    cred = credentials.Certificate("app/configs/firebase.json")
    initialize_app(cred,{
    'storageBucket': 'portfolio-8ccd0.com'
})

def upload_to_firebase(file: UploadFile):
    try:
        # Upload file to Firebase Storage
        #todo: change the storage path
        input_file = ""
        bucket = storage.bucket()
        storage_path = f""
        blob = bucket.blob(storage_path)
        content_type = mimetypes.guess_type(file.filename)[0]
        blob.upload_from_file(file.file, content_type=content_type)
        return storage_path
    except:
        raise HTTPException(status_code=500, detail="Error in uploading file to Firebase Storage.")

    
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
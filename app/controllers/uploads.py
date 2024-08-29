from fastapi import APIRouter

router = APIRouter()

@router.get("/upload")
def make_upload():
    return {"message": "This is the upload endpoint"}
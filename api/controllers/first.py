from fastapi import APIRouter

router = APIRouter()

@router.get("/first")
def read_first():
    return {"message": "This is the first endpoint"}
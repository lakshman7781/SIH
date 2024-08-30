from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "This is the root endpoint"}

@router.get("/health")
def read_health():
    return {"message": "This is the health endpoint"}
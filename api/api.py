from fastapi import APIRouter
from .controllers import first

api_router = APIRouter()

api_router.include_router(first.router, tags=["first"])


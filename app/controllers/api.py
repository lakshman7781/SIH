from fastapi import APIRouter
from .import health, uploads

api_router = APIRouter()

api_router.include_router(health.router, tags=["health"], prefix="/health")
api_router.include_router(uploads.router, tags=["uploads"], prefix="/uploads")


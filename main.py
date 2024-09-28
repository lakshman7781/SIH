import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controllers.api import api_router
from dotenv import load_dotenv
from app.integrations.firebase import initialize_firebase_app

load_dotenv(".env")

app = FastAPI()

allowed_origins = [
    "http://localhost",
    "http://localhost:3000",
    "https://sih-fe.vercel.app",
]

APP_ENVIRONMENT = os.environ.get("APP_ENVIRONMENT", None)

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

# Initialize Firebase app
initialize_firebase_app()

app.include_router(api_router, prefix='')

if APP_ENVIRONMENT == APP_ENVIRONMENT:
    print('ENVIRONMENT is APP_ENVIRONMENT')

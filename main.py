import uvicorn
from fastapi import FastAPI
from api.api import api_router

app = FastAPI()
app.include_router(api_router, prefix='')

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
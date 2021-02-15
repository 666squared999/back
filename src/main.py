from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from pathlib import Path
import asyncio
import os

app = FastAPI()

load_dotenv(dotenv_path=Path('..') / '.env')

origins = os.getenv('CORS_ALLOWED_HOSTS') 
origins = [
    '*',
    'http://localhost',
    'http://localhost:3000',
    *(origins.split(';') if origins is not None else [])
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
)

# @app.get('/somerequest')
# async def bw(wmin: float = None, wmax: float = None, allres: bool = False):
#   pass

@app.get("/")
async def root():
    return {"message": "Hello World"}

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from settings import origins

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

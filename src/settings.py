from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv(dotenv_path=Path('..') / '.env')

origins = os.getenv('CORS_ALLOWED_HOSTS') 
origins = [
    'http://localhost',
    'http://localhost:3000',
    *(origins.split(';') if origins is not None else [])
]

ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
SECRET_KEY = os.getenv("SECRET_KEY")
DB_PASS = os.getenv("DB_PASS")

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

COOKIE_AUTHORIZATION_NAME = "Authorization"
COOKIE_DOMAIN = "squared.cf"

PROTOCOL = "https://"
FULL_HOST_NAME = "scuared.cf"
PORT_NUMBER = 80

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRETS_JSON = "./secret.json"

API_LOCATION = f"{PROTOCOL}{FULL_HOST_NAME}:{PORT_NUMBER}"
SWAP_TOKEN_ENDPOINT = "/swap_token"
SUCCESS_ROUTE = "/users/me"
ERROR_ROUTE = "/login_error"

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
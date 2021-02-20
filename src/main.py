from fastapi.middleware.cors import CORSMiddleware

import httplib2
from oauth2client import client
from google.oauth2 import id_token
from google.auth.transport import requests

from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder

from starlette.responses import JSONResponse, HTMLResponse
from starlette.requests import Request

from settings import (
    CLIENT_ID,
    SWAP_TOKEN_ENDPOINT,
    ERROR_ROUTE,
    origins,
    CLIENT_SECRETS_JSON,
    ACCESS_TOKEN_EXPIRE_MINUTES,
    COOKIE_DOMAIN,
    COOKIE_AUTHORIZATION_NAME,
)

from utils.authentication import (
    google_login_javascript_client,
    google_login_javascript_server,
    authenticate_user_email,
    fake_users_db,
    create_access_token,
)

from models.users import Token
from datetime import timedelta

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
)


@app.get("/google_login_client", tags=["security"])
def google_login_client():
    return HTMLResponse(google_login_javascript_client)


@app.get("/google_login_server", tags=["security"])
def google_login_server():
    return HTMLResponse(google_login_javascript_server)


@app.post(f"{SWAP_TOKEN_ENDPOINT}", response_model=Token, tags=["security"])
async def swap_token(request: Request = None):
    if not request.headers.get("X-Requested-With"):
        raise HTTPException(status_code=400, detail="Incorrect headers")

    google_client_type = request.headers.get("X-Google-OAuth2-Type")

    if google_client_type == 'server':
        try:
            body_bytes = await request.body()
            auth_code = jsonable_encoder(body_bytes)

            credentials = client.credentials_from_clientsecrets_and_code(
                CLIENT_SECRETS_JSON, ["profile", "email"], auth_code
            )

            http_auth = credentials.authorize(httplib2.Http())

            email = credentials.id_token["email"]

        except:
            raise HTTPException(status_code=400, detail="Unable to validate social login")


    if google_client_type == 'client':
        body_bytes = await request.body()
        auth_code = jsonable_encoder(body_bytes)

        try:
            idinfo = id_token.verify_oauth2_token(auth_code, requests.Request(), CLIENT_ID)

            # Or, if multiple clients access the backend server:
            # idinfo = id_token.verify_oauth2_token(token, requests.Request())
            # if idinfo['aud'] not in [CLIENT_ID_1, CLIENT_ID_2, CLIENT_ID_3]:
            #     raise ValueError('Could not verify audience.')

            if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                raise ValueError('Wrong issuer.')

            # If auth request is from a G Suite domain:
            # if idinfo['hd'] != GSUITE_DOMAIN_NAME:
            #     raise ValueError('Wrong hosted domain.')

            if idinfo['email'] and idinfo['email_verified']:
                email = idinfo.get('email')

            else:
                raise HTTPException(status_code=400, detail="Unable to validate social login")

        except:
            raise HTTPException(status_code=400, detail="Unable to validate social login")

    authenticated_user = authenticate_user_email(fake_users_db, email)

    if not authenticated_user:
        raise HTTPException(status_code=400, detail="Incorrect email address")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": authenticated_user.email}, expires_delta=access_token_expires
    )

    token = jsonable_encoder(access_token)

    response = JSONResponse({"access_token": token, "token_type": "bearer"})

    response.set_cookie(
        COOKIE_AUTHORIZATION_NAME,
        value=f"Bearer {token}",
        domain=COOKIE_DOMAIN,
        httponly=True,
        max_age=1800,
        expires=1800,
    )
    return response


@app.get(f"{ERROR_ROUTE}", tags=["security"])
async def login_error():
    return "Something went wrong logging in!"


@app.get("/logout", tags=["security"])
async def route_logout_and_remove_cookie():
    response = JSONResponse({"status": "success"})
    response.delete_cookie(COOKIE_AUTHORIZATION_NAME, domain=COOKIE_DOMAIN)
    return response

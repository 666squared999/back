from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from schemas.users import UsersList, UserCreate, TokenData, Token
from fastapi.security import OAuth2PasswordRequestForm
from database import SessionLocal, engine
from utils.authentication import (
    get_password_hash,
    get_post_by_id,
    get_user_by_login,
    get_current_user
)

from settings import origins

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# user related
@app.get("/users/", response_model=UsersList)
def read_users(limit: int=100, db: Session=Depends(get_db)):
    return get_users(db, limit=limit)


@app.get("/users/me/", response_model=TokenData)
async def read_users_me(current_user=Depends(get_current_user)):
    return current_user


@app.post("/users/new_user",
          response_model=UserCreate,
          status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate,
                db: Session=Depends(get_db)):
    db_user = get_user_by_login(db, login=user.login)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Login already registered"
        )
    return create_user(db=db, user=user)


# token
@app.post("/token", response_model=Token)
async def login_for_access_token(
                form_data: OAuth2PasswordRequestForm=Depends(),
                db: Session=Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(db=db,
                                            data={"sub": user.login},
                                            expires_delta=access_token_expires)
    return Token(access_token=access_token, token_type="bearer")
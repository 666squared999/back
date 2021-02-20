from sqlalchemy.orm import Session
from passlib.context import CryptContext
import models, settings
from datetime import datetime, timedelta
import jwt
from jwt import PyJWTError
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from database import SessionLocal, engine
from schemas.users import (
    UserCreate,
    Token
)

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_users(db: Session, limit: int = 100):
    users_lists = db.query(models.User.login).limit(limit).all()
    users_list = []
    for i in users_lists:
        users_list.append(i[0])
    return UsersList(all_users_list=users_list)


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
    except PyJWTError:
        raise credentials_exception
    return TokenData(current_user=username)


def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(login=user.login, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return UserCreate(login=user.login, password=hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_user_by_login(db: Session, login: str):
    return db.query(models.User).filter(models.User.login == login).first()


def get_post_by_id(db: Session, post_id: int):
    return db.query(models.Post).filter(models.Post.id == post_id).first()


def authenticate_user(db: Session, login: str, password: str):
    user = get_user_by_login(db, login)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(db: Session,
                        data: dict,
                        expires_delta: timedelta = None):
    db_post = models.Login(login=data["sub"])
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
from pydantic import BaseModel, Field
from typing import List


class UserCreate(BaseModel):
    login: str = Field(..., min_length=2, max_length=30)
    password: str = Field(..., min_length=5)


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    current_user: str = None


class LastLogin(BaseModel):
    login: str
    date_time: str


class UsersList(BaseModel):
    all_users_list: List[str]

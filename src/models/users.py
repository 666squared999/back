from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from database import Base


class User(Base):
    __tablename__ = "User"

    login = Column(String(30), primary_key=True)
    hashed_password = Column(Text)


class Login(Base):
    __tablename__ = "Login"

    login = Column(String(30), primary_key=True)
    date_time = Column(DateTime, default=datetime.utcnow)
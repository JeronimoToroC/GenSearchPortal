"""Models for the application."""

from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    """User model"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

class Otp(Base):
    """Otp model"""
    __tablename__ = "otps"

    id = Column(Integer, primary_key=True, index=True)
    jwt = Column(String, index=True)
    code = Column(String)

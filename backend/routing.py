"""Main routing."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from dtos.user_dto import UserLoginDto
from logic.user_logic import UserLogic

app_router = APIRouter()

@app_router.get("/", summary="Main route", tags=["Main"])
def main():
    """Main route."""
    return {"message": "Hello World"}

@app_router.post("/login", summary="Login user", tags=["Auth"])
def login(user_data: UserLoginDto, db: Session = Depends(get_db)):
    """Login user endpoint."""
    return UserLogic.login(db, user_data)

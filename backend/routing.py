"""Main routing."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from dtos.user_dto import UserLoginDto
from dtos.user_dto import UserRegisterDto
from logic.user_logic import UserLogic
from dtos.user_dto import VerifyOtpDto

app_router = APIRouter()

@app_router.get("/", summary="Main route", tags=["Main"])
def main():
    """Main route."""
    return {"message": "Hello World"}

@app_router.post("/login", summary="Login user", tags=["Auth"])
def login(user_data: UserLoginDto, db: Session = Depends(get_db)):
    """Login user endpoint."""
    return UserLogic.login(db, user_data)

@app_router.post("/register", summary="Register user", tags=["Auth"])
def register(user_data: UserRegisterDto, db: Session = Depends(get_db)):
    """Registrar usuario y enviar OTP."""
    return UserLogic.register(db, user_data)

@app_router.post("/verify-otp", summary="Verificar OTP", tags=["Auth"])
def verify_otp(otp_data: VerifyOtpDto, db: Session = Depends(get_db)):
    """
    Endpoint para verificar el OTP y registrar al usuario.
    """
    return UserLogic.verify_otp(db, otp_data.email, otp_data.otp_code)
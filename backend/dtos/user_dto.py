"""User data transfer objects."""

from pydantic import BaseModel, EmailStr

class UserLoginDto(BaseModel):
    """User login data."""
    email: EmailStr
    password: str

class UserRegisterDto(BaseModel):
    name: str
    email: EmailStr
    password: str
    
class VerifyOtpDto(BaseModel):
    email: str
    otp_code: str

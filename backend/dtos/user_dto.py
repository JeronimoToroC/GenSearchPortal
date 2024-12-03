"""User data transfer objects."""

from pydantic import BaseModel, EmailStr

class UserLoginDto(BaseModel):
    """User login data."""
    email: EmailStr
    password: str

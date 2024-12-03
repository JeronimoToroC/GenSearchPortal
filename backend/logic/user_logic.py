"""User logic."""

from sqlalchemy.orm import Session
from fastapi import HTTPException
from dtos.user_dto import UserLoginDto
from models import User


class UserLogic:
    """User logic."""

    @staticmethod
    def login(db: Session, user_data: UserLoginDto):
        """Login user."""

        # Buscar usuario por email
        user = db.query(User).filter(User.email == user_data.email).first()

        # Verificar si el usuario existe y la contraseña coincide
        if not user or user.password != user_data.password:
            raise HTTPException(
                status_code=401,
                detail="Credenciales incorrectas"
            )

        # Si todo está bien, retornar el usuario (sin la contraseña)
        return {
            "id": user.id,
            "name": user.name,
            "email": user.email
        }

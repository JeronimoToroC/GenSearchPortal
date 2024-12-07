"""User logic."""

import random
from werkzeug.security import check_password_hash
from pathlib import Path
import shutil
from fastapi import UploadFile
import string
from sqlalchemy.orm import Session
from fastapi import HTTPException
from dtos.user_dto import UserLoginDto, UserRegisterDto
from models import User, Otp
from werkzeug.security import generate_password_hash
import jwt
from utils.email_utils import send_email
from datetime import datetime, timedelta, timezone
import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

class UserLogic:
    """User logic."""

    @staticmethod
    def login(db: Session, user_data: UserLoginDto):
        """Login user."""

        # Buscar usuario por email
        user = db.query(User).filter(User.email == user_data.email).first()

        # Verificar si el usuario existe y la contraseña coincide
        if not user or not check_password_hash(user.password, user_data.password):
            raise HTTPException(
                status_code=401,
                detail="Credenciales incorrectas"
            )
        return {
            "id": user.id,
            "name": user.name,
            "email": user.email
        }

    @staticmethod
    def register(db: Session, user_data: UserRegisterDto):
        """Registrar un nuevo usuario."""

        if db.query(User).filter(User.email == user_data.email).first():
            raise HTTPException(status_code=400, detail="El correo ya está registrado.")

        payload = {
            "name": user_data.name,
            "email": user_data.email,
            "password": user_data.password,
            "exp": datetime.now(timezone.utc) + timedelta(minutes=15),
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

        # Generar OTP único
        otp_code = ''.join(random.choices(string.digits, k=6))

        # Guardar OTP y JWT en la base de datos
        otp = Otp(jwt=token, code=otp_code)
        db.add(otp)
        db.commit()

        # Enviar OTP al correo
        email_subject = "Tu código de verificación"
        email_message = f"Hola {user_data.name},\n\nTu código de verificación es: {otp_code}\n\nGracias."
        send_email(user_data.email, email_subject, email_message)

        return {"message": "OTP enviado al correo."}


    @staticmethod
    def verify_otp(db: Session, email: str, otp_code: str):
        """Verificar el OTP y registrar al usuario si es válido."""

        # Buscar el OTP asociado al correo
        otp_entry = db.query(Otp).filter(Otp.code == otp_code).first()

        if not otp_entry:
            raise HTTPException(status_code=400, detail="OTP inválido o expirado")

        # Decodificar el token JWT asociado al OTP
        try:
            payload = jwt.decode(otp_entry.jwt, SECRET_KEY, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=400, detail="El token ha expirado")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=400, detail="Token inválido")

        # Verificar que el correo coincida
        if payload["email"] != email:
            raise HTTPException(status_code=400, detail="El correo no coincide con el token")

        # Registrar al usuario
        hashed_password = generate_password_hash(payload["password"])  # Asegúrate de que el payload tenga contraseña
        user = User(name=payload["name"], email=payload["email"], password=hashed_password)
        db.add(user)
        db.commit()

        # Eliminar el OTP para evitar reusos
        db.delete(otp_entry)
        db.commit()

        return {"message": "Usuario registrado exitosamente"}

    @staticmethod
    async def upload_vcf(file: UploadFile):
        """Procesar la subida de archivo VCF."""
        try:
            # Verificar extensión
            if not file.filename.endswith('.vcf'):
                raise HTTPException(
                    status_code=400,
                    detail="El archivo debe tener extensión .vcf"
                )

            # Ruta donde se guardará el archivo
            DATA_DIR = Path("data")
            DATA_DIR.mkdir(exist_ok=True)
            file_path = DATA_DIR / file.filename

            # Guardar archivo en chunks para manejar archivos grandes
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)

            return {
                "mensaje": "Archivo subido exitosamente",
                "nombre_archivo": file.filename,
                "ruta": str(file_path)
            }

        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Error al subir archivo: {str(e)}"
            )

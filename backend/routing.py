"""Main routing."""

from pathlib import Path
import shutil
from fastapi import APIRouter, Depends, File, UploadFile
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database import get_db
from dtos.user_dto import UserLoginDto, UserRegisterDto, VerifyOtpDto
from logic.user_logic import UserLogic

app_router = APIRouter()

# Crear directorio data si no existe
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

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

@app_router.post("/upload-vcf", summary="Subir archivo VCF", tags=["Genome"])
async def upload_vcf(file: UploadFile = File(...)):
    """Endpoint para subir archivo VCF."""
    try:
        # Verificar extensión
        if not file.filename.endswith('.vcf'):
            return JSONResponse(
                status_code=400,
                content={"error": "El archivo debe tener extensión .vcf"}
            )

        # Ruta donde se guardará el archivo
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
        return JSONResponse(
            status_code=500,
            content={"error": f"Error al subir archivo: {str(e)}"}
        )

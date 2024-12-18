"""Main routing."""

from pathlib import Path
from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session
from database import get_db
from dtos.user_dto import UserLoginDto, UserRegisterDto, VerifyOtpDto
from logic.user_logic import UserLogic
from logic.vcf_logic import VcfLogic
from logic.genome_logic import obtener_genomas_por_coincidencia

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
    await VcfLogic.upload_vcf_and_insert_data(file)
    return {"message": "Archivo VCF subido exitosamente"}

@app_router.get("/genomes", summary="Obtener genomas por coincidencia", tags=["Genome"])
def get_genomes_by_coincidence(
    coincidence: str,
    items_per_page: int = 10,
    page: int = 1
):
    """
    Obtener genomas por coincidencia con paginación.
    
    Args:
        coincidence (str): Texto a buscar
        items_per_page (int): Número de items por página (default: 10)
        page (int): Número de página actual (default: 1)
    """
    return obtener_genomas_por_coincidencia(coincidence, items_per_page, page)

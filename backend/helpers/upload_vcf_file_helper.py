from pathlib import Path
import shutil
from fastapi import HTTPException, UploadFile

async def upload_file_vcf(file: UploadFile):
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
"""VCF file handling logic."""

from fastapi import UploadFile
from helpers.upload_vcf_file_helper import upload_file_vcf
from helpers.insert_data_in_db_helper import procesar_archivo_vcf

class VcfLogic:
    """VCF file handling logic."""

    @staticmethod
    async def upload_vcf_and_insert_data(file: UploadFile):
        """Procesar la subida de archivo VCF."""
        # await upload_file_vcf(file)
        # procesar_archivo_vcf(file.filename)
        procesar_archivo_vcf("cabernetSauvignon.vcf")

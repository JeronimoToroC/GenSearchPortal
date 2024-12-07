# Para cargar el archivo vcf

curl -X POST "http://localhost:8001/upload-vcf" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "file=@archivo.vcf"

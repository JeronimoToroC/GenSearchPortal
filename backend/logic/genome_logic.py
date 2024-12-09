## REGISTRAR NUEVA BASE DE DATOS SQLITE
import sqlite3

# Conectar o crear la base de datos
db_path = "cabernetSauvignon.db"
# conn = sqlite3.connect(db_path)
# cursor = conn.cursor()

# # Crear la tabla principal
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS vcf_data (
#     CHROM TEXT,
#     POS INTEGER,
#     ID TEXT,
#     REF TEXT,
#     ALT TEXT,
#     QUAL REAL,
#     FILTER TEXT,
#     INFO TEXT,
#     FORMAT TEXT,
#     output_CH1 TEXT,
#     output_CH10 TEXT,
#     output_CH11 TEXT,
#     output_CH12 TEXT,
#     output_CH13 TEXT,
#     output_CH14 TEXT,
#     output_CH15 TEXT,
#     output_CH16 TEXT,
#     output_CH17 TEXT,
#     output_CH18 TEXT,
#     output_CH19 TEXT,
#     output_CH2 TEXT,
#     output_CH20 TEXT,
#     output_CH3 TEXT,
#     output_CH4 TEXT,
#     output_CH5 TEXT,
#     output_CH6 TEXT,
#     output_CH7 TEXT,
#     output_CH8 TEXT,
#     output_CH9 TEXT
# );
# """)

# # Crear índices para optimización
# cursor.execute("CREATE INDEX IF NOT EXISTS idx_chrom ON vcf_data (CHROM);")
# cursor.execute("CREATE INDEX IF NOT EXISTS idx_filter ON vcf_data (FILTER);")
# cursor.execute("CREATE INDEX IF NOT EXISTS idx_info ON vcf_data (INFO);")
# cursor.execute("CREATE INDEX IF NOT EXISTS idx_format ON vcf_data (FORMAT);")

# # Función para leer el archivo VCF e insertar los datos en la tabla
# def parse_vcf_to_sqlite(file_path, conn):
#     cursor = conn.cursor()
#     with open(file_path, "r") as f:
#         for line in f:
#             if line.startswith("##"):
#                 continue
#             elif line.startswith("#"):
#                 header = line.strip().split("\t")
#                 continue
            
#             parts = line.strip().split("\t")
#             # Asegurarse de que tengamos suficientes valores
#             while len(parts) < 29:  # Añadir valores nulos si faltan columnas
#                 parts.append(None)
            
#             cursor.execute("""
#                 INSERT INTO vcf_data (
#                     CHROM, POS, ID, REF, ALT, QUAL, FILTER, INFO, FORMAT,
#                     output_CH1, output_CH10, output_CH11, output_CH12, output_CH13, output_CH14, 
#                     output_CH15, output_CH16, output_CH17, output_CH18, output_CH19, 
#                     output_CH2, output_CH20, output_CH3, output_CH4, output_CH5, output_CH6, 
#                     output_CH7, output_CH8, output_CH9
#                 ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
#             """, (
#                 parts[0],  # CHROM
#                 int(parts[1]),  # POS
#                 parts[2],  # ID
#                 parts[3],  # REF
#                 parts[4],  # ALT
#                 float(parts[5]) if parts[5] != "." else None,  # QUAL
#                 parts[6],  # FILTER
#                 parts[7],  # INFO
#                 parts[8],  # FORMAT
#                 *parts[9:29]  # Limitar a exactamente las columnas necesarias
#             ))
#     conn.commit()

# # Ruta al archivo VCF
# vcf_file = "cabernetSauvignon.vcf"
# parse_vcf_to_sqlite(vcf_file, conn)
# print("Datos insertados en SQLite.")

# # Cerrar la conexión
# conn.close()


## BUSCAR PATRON EN LA BASE DE DATOS
# Conectar para consultas
# Parámetros de paginado
page_size = 6  # Número de ítems por página
page_number = 2  # Página que deseas consultar (inicia en 1)

# Calcular el OFFSET
offset = (page_number - 1) * page_size

# Consulta con paginado
query = """
SELECT CHROM, POS, REF, ALT, FILTER, INFO, FORMAT
FROM vcf_data
WHERE CHROM LIKE ?
   OR REF LIKE ?
   OR ALT LIKE ?
   OR FILTER LIKE ?
   OR INFO LIKE ?
   OR FORMAT LIKE ?
LIMIT ? OFFSET ?;
"""
params = ("%CGT%", "%CGT%", "%CGT%", "%CGT%", "%CGT%", "%CGT%", page_size, offset)

# Ejecutar consulta
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
cursor.execute(query, params)

# Mostrar resultados
results = cursor.fetchall()
for row in results:
    print(row)

# Cerrar conexión
conn.close()

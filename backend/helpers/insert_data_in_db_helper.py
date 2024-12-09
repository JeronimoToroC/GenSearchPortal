"""Utilidades para insertar datos del archivo VCF en la base de datos SQLite."""

import sqlite3
from pathlib import Path
from helpers.obtener_valor_columna_helper import ObtenerValorColumnaHelper

obtener_valor_columna_helper: ObtenerValorColumnaHelper = None

def crear_base_datos():
    """Crear la base de datos e índices."""
    # Asegurar que el directorio data existe
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)

    # Crear la base de datos en el directorio data
    db_path = data_dir / "genomes.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Crear la tabla principal
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vcf_data (
        CHROM TEXT,
        POS INTEGER,
        ID TEXT,
        REF TEXT,
        ALT TEXT,
        QUAL REAL,
        FILTER TEXT,
        INFO TEXT,
        FORMAT TEXT,
        output_1 TEXT,
        output_2 TEXT,
        output_3 TEXT,
        output_4 TEXT,
        output_5 TEXT,
        output_6 TEXT,
        output_7 TEXT,
        output_8 TEXT,
        output_9 TEXT,
        output_10 TEXT,
        output_11 TEXT,
        output_12 TEXT,
        output_13 TEXT,
        output_14 TEXT,
        output_15 TEXT,
        output_16 TEXT,
        output_17 TEXT,
        output_18 TEXT,
        output_19 TEXT,
        output_20 TEXT,
        output_21 TEXT,
        output_22 TEXT,
        output_23 TEXT,
        output_24 TEXT,
        output_25 TEXT
    );
    """)

    # Crear índices para optimización
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_chrom ON vcf_data (CHROM);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_filter ON vcf_data (FILTER);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_info ON vcf_data (INFO);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_format ON vcf_data (FORMAT);")

    conn.commit()
    return conn

def insertar_datos_vcf(conn, file_path):
    """Insertar datos del archivo VCF en la base de datos."""
    cursor = conn.cursor()

    with open(file_path, "r") as f:
        for line in f:
            if line.startswith("##"):
                continue
            elif line.startswith("#"):
                header = line.strip()
                global obtener_valor_columna_helper
                obtener_valor_columna_helper = ObtenerValorColumnaHelper(header)
                continue

            parts = line.strip().split("\t")

            cursor.execute("""
                INSERT INTO vcf_data (
                    CHROM, POS, ID, REF, ALT, QUAL, FILTER, INFO, FORMAT,
                    output_1, output_2, output_3, output_4, output_5, output_6, output_7,
                    output_8, output_9, output_10, output_11, output_12, output_13, output_14,
                    output_15, output_16, output_17, output_18, output_19, output_20, 
                    output_21, output_22, output_23, output_24, output_25
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
            """,
            _obtener_valores_de_toda_la_fila(parts)
            )

    conn.commit()

def _obtener_valores_de_toda_la_fila(fila: list[str]) -> tuple:
    """Obtener los valores de toda la fila."""
    valores = [
        obtener_valor_columna_helper.obtener_valor_de_columna("CHROM", fila),
        obtener_valor_columna_helper.obtener_valor_de_columna("POS", fila),
        obtener_valor_columna_helper.obtener_valor_de_columna("ID", fila),
        obtener_valor_columna_helper.obtener_valor_de_columna("REF", fila),
        obtener_valor_columna_helper.obtener_valor_de_columna("ALT", fila),
        obtener_valor_columna_helper.obtener_valor_de_columna("QUAL", fila),
        obtener_valor_columna_helper.obtener_valor_de_columna("FILTER", fila),
        obtener_valor_columna_helper.obtener_valor_de_columna("INFO", fila),
        obtener_valor_columna_helper.obtener_valor_de_columna("FORMAT", fila),
    ]

    for i in range(1, 26):
        valores.append(obtener_valor_columna_helper.obtener_valor_de_columna(f"output_{i}", fila))

    return tuple(valores)

def obtener_o_crear_base_de_datos():
    """Obtener conexión a la base de datos. Si no existe, la crea."""
    try:
        # Asegurar que el directorio data existe
        data_dir = Path("data")
        data_dir.mkdir(exist_ok=True)

        # Ruta de la base de datos
        db_path = data_dir / "genomes.db"

        # Si la base de datos no existe, crearla con la estructura
        if not db_path.exists():
            return crear_base_datos()

        # Si ya existe, simplemente conectar y devolver la conexión
        return sqlite3.connect(db_path)

    except Exception as e:
        print(f"Error al obtener la base de datos: {str(e)}")
        return None

def procesar_archivo_vcf(archivo_vcf: str):
    """Función principal para procesar el archivo VCF."""
    try:
        # Verificar si existe el archivo
        vcf_path = Path("data/" + archivo_vcf)
        if not vcf_path.exists():
            print(f"Error: No se encuentra el archivo en {vcf_path}")
            return False

        # Crear base de datos e índices
        conn = obtener_o_crear_base_de_datos()

        # Insertar datos
        insertar_datos_vcf(conn, vcf_path)

        print("Datos insertados exitosamente en la base de datos")
        conn.close()

        # Borrar el archivo VCF después de procesarlo exitosamente
        vcf_path.unlink()
        print(f"Archivo {archivo_vcf} eliminado exitosamente")
        return True

    except Exception as e:
        print(f"Error al procesar el archivo VCF: {e}")
        return False

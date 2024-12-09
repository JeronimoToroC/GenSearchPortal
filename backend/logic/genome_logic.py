"""
Logica para obtener genomas por coincidencia.
"""

import sqlite3

def obtener_genomas_por_coincidencia(coincidencia: str):
    """Obtener genomas por coincidencia."""
    page_size = 6
    page_number = 2
    offset = (page_number - 1) * page_size
    db_path = "data/genomes.db"

    query = """
    SELECT CHROM, POS, REF, ALT, FILTER, INFO, FORMAT,
        output_1, output_2, output_3, output_4, output_5, 
        output_6, output_7, output_8, output_9, output_10, 
        output_11, output_12, output_13, output_14,
        output_15, output_16, output_17, output_18, output_19, 
        output_20, output_21, output_22, output_23, output_24, output_25
    FROM vcf_data
    WHERE CHROM LIKE ?
       OR REF LIKE ?
       OR ALT LIKE ?
       OR FILTER LIKE ?
       OR INFO LIKE ?
       OR FORMAT LIKE ?
    LIMIT ? OFFSET ?;
    """
    params = (coincidencia, coincidencia, coincidencia, coincidencia, coincidencia, coincidencia, page_size, offset)

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(query, params)
    results = cursor.fetchall()
    return results

"""
Logica para obtener genomas por coincidencia.
"""

import sqlite3

def obtener_genomas_por_coincidencia(coincidencia: str,
                                     items_por_pagina: int = 10,
                                     pagina_actual: int = 1):
    """
    Obtener genomas por coincidencia con paginación.
    
    Args:
        coincidencia (str): Texto a buscar
        items_por_pagina (int): Número de items por página
        pagina_actual (int): Número de página actual
    """
    offset = (pagina_actual - 1) * items_por_pagina
    db_path = "data/genomes.db"

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Consulta principal con paginación
        data_query = """
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

        search_pattern = f"%{coincidencia}%"
        data_params = (search_pattern,) * 6 + (items_por_pagina, offset)

        # Obtener datos paginados
        cursor.execute(data_query, data_params)
        resultados = cursor.fetchall()

        return {
            "pagina_actual": pagina_actual,
            "items_por_pagina": items_por_pagina,
            "resultados": resultados
        }

    except sqlite3.Error as e:
        print(f"Error en la base de datos: {e}")
        return None
    finally:
        if conn:
            conn.close()

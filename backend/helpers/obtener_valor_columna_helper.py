"""
Este helper se encarga de obtener el valor de una columna en base a su nombre.
"""

class GenomeColumnModel:
    """
    Esta clase representa una columna en el genoma.
    """
    def __init__(self, nombre: str, indice: int):
        self.nombre = nombre
        self.indice = indice

class ObtenerValorColumnaHelper:
    """
    Esta clase se encarga de obtener el valor de una columna en base a su nombre.
    """
    encabezado = ''
    columnas_del_encabezado = list[str]
    columnas_definitivas: list[GenomeColumnModel]

    def __init__(self, encabezado: str):
        self.encabezado = encabezado
        self._partir_encabezado_en_columnas()
        self._definir_todas_las_columnas()

    def _partir_encabezado_en_columnas(self):
        self.columnas_del_encabezado = self.encabezado.split('\t')

    def _definir_todas_las_columnas(self):
        self.columnas_definitivas = self._definir_columnas_estandar()
        self.columnas_definitivas.extend(self._definir_las_columnas_outputs())

    def _definir_columnas_estandar(self):
        """
        Define las columnas estándar para el genoma.
        """
        columnas_estandar: list[GenomeColumnModel] = [
            GenomeColumnModel("CHROM", 0),
            GenomeColumnModel("POS", 1),
            GenomeColumnModel("ID", 2),
            GenomeColumnModel("REF", 3),
            GenomeColumnModel("ALT", 4),
            GenomeColumnModel("QUAL", 5),
            GenomeColumnModel("FILTER", 6),
            GenomeColumnModel("INFO", 7),
            GenomeColumnModel("FORMAT", 8),
        ]
        return columnas_estandar

    def _definir_las_columnas_outputs(self):
        """
        Define las columnas de salida para el genoma.
        """
        columnas_outputs = []
        for i in range(9, 33):
            indice = self._obtener_indice_de_columna_por_numero_de_output(i)
            columnas_outputs.append(GenomeColumnModel(f"output_{i}", indice))
        return columnas_outputs

    def _obtener_indice_de_columna_por_numero_de_output(self, numero: int):
        """
        Obtiene el índice de una columna por su número de salida.

        Ejemplo:
        columnas_del_encabezado = ['CHROM', 'POS', 'ID', 'output_CS9', 'output_CH15', 'output_CS10', 'output_CH16']
        numero_output_a_buscar = 15
        indice_a_retornar = 4
        """
        indice_a_retornar = -1
        for columna in self.columnas_del_encabezado:
            if columna.startswith("output_") and int(columna[9:]) == numero:
                indice_a_retornar = self.columnas_del_encabezado.index(columna)
                break
        return indice_a_retornar

    def obtener_indice_de_columna_por_nombre(self, nombre: str) -> int | None:
        """
        Obtiene el índice de una columna por su nombre.
        """
        for columna in self.columnas_definitivas:
            if columna.nombre == nombre:
                return columna.indice
        return None

    def obtener_valor_de_columna(self, nombre: str, fila: list[str]) -> str:
        """
        Obtiene el valor de una columna por su nombre.
        """
        indice = self.obtener_indice_de_columna_por_nombre(nombre)
        if indice is None:
            return ""
        return fila[indice]

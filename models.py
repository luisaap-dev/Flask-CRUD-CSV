import csv
import os

class CSVModel:
    def __init__(self):
        self.ruta_archivo_datos = os.path.join(os.path.dirname(__file__), 'data', 'datos.csv')
        self.codificacion_csv = 'utf-8-sig'
        self.cabecera = ['id', 'nombre', 'apellidos', 'email', 'telefono', 'sexo', 'direccion', 'ciudad', 'pais']
        self._verificar_archivo_csv()

    def _verificar_archivo_csv(self):
        """Crea el archivo CSV si no existe y asegura que tenga la cabecera."""
        if not os.path.exists(self.ruta_archivo_datos):
            self._crear_archivo_csv()

    def _crear_archivo_csv(self):
        """Crea el archivo CSV con la cabecera."""
        with open(self.ruta_archivo_datos, 'w', newline='', encoding=self.codificacion_csv) as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=self.cabecera)
            escritor.writeheader()

    def _abrir_archivo(self, modo):
        """Abre el archivo CSV en el modo especificado."""
        return open(self.ruta_archivo_datos, modo, newline='', encoding=self.codificacion_csv)

    def _obtener_lector_csv(self):
        """Obtiene un lector CSV para leer el archivo."""
        archivo = self._abrir_archivo('r')
        return archivo, csv.DictReader(archivo)

    def _obtener_todas_las_filas(self):
        """Obtiene todas las filas del archivo CSV."""
        archivo, lector = self._obtener_lector_csv()
        filas = [fila for fila in lector]
        archivo.close()
        return filas

    def _guardar_filas(self, filas):
        """Guarda las filas en el archivo CSV."""
        with self._abrir_archivo('w') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=self.cabecera)
            escritor.writeheader()
            escritor.writerows(filas)

    def obtener_todos_los_datos(self):
        """Obtiene todos los registros del archivo CSV."""
        return self._obtener_todas_las_filas()

    def obtener_datos(self, id):
        """Obtiene un registro específico por ID."""
        for fila in self._obtener_todas_las_filas():
            if fila['id'] == id:
                return fila
        return None

    def agregar_datos(self, datos):
        """Agrega un nuevo registro al archivo CSV."""
        filas = self._obtener_todas_las_filas()
        datos['id'] = str(self.obtener_ultimo_id() + 1)
        filas.append(datos)
        self._guardar_filas(filas)

    def actualizar_datos(self, id, datos_actualizados):
        """Actualiza un registro existente por ID."""
        filas = []
        encontrado = False
        for fila in self._obtener_todas_las_filas():
            if fila['id'] == id:
                datos_actualizados['id'] = id
                filas.append(datos_actualizados)
                encontrado = True
            else:
                filas.append(fila)
        if encontrado:
            self._guardar_filas(filas)
            return True
        return False

    def eliminar_datos(self, id):
        """Elimina un registro por ID."""
        filas = [fila for fila in self._obtener_todas_las_filas() if fila['id'] != id]
        if len(filas) < len(self._obtener_todas_las_filas()):  # Verifica si se eliminó algún dato
            self._guardar_filas(filas)
            return True
        return False

    def obtener_ultimo_id(self):
        """Obtiene el último ID utilizado en el archivo CSV."""
        ultimo_id = 0
        for fila in self._obtener_todas_las_filas():
            try:
                ultimo_id = max(ultimo_id, int(fila['id']))
            except ValueError:
                continue  # Ignora filas con IDs no válidos
        return ultimo_id

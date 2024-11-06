# Flask-CRUD-CSV

Flask-CRUD-CSV es una aplicación web simple desarrollada con Flask que permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre un archivo CSV. Los usuarios pueden agregar, editar, eliminar y visualizar registros de personas, que contienen información como nombre, apellidos, email, teléfono, sexo, dirección, ciudad y país.

## Funcionalidades

- **Crear Registro**: Permite agregar nuevos registros de personas.
- **Leer Registros**: Muestra la lista de registros existentes.
- **Actualizar Registro**: Permite modificar los datos de un registro seleccionado.
- **Eliminar Registro**: Permite eliminar un registro existente.

## Requisitos Previos

- Python 3.x
- Flask (Instalable mediante `pip install flask`)

## Instalación y Ejecución

1. Clona este repositorio en tu máquina local:

```shell
   git clone https://github.com/luisaap-dev/Flask-CRUD-CSV
```
2. Accede al directorio del repositorio:

```shell
cd Flask-CRUD-CSV
```

3. Crear entorno virtual (opcional pero recomendado)
- (windows)
```shell
python -m venv nombre_del_entorno
```
- (linux)
```shell
python3 -m venv nombre_del_entorno
```

4. Activar el entorno virtual (opcional pero recomendado):

- Windows (CMD):
```shell
nombre_del_entorno\Scripts\activate
```
- Windows (PowerShell):
```shell
.\nombre_del_entorno\Scripts\Activate
```
- Linux/Ubuntu:
```shell
source nombre_del_entorno/bin/activate
```

5. Instala las dependencias utilizando `pip`:

```shell
pip install -r requirements.txt
```

6. Ejecuta la aplicación:

```shell
python app.py
```

La aplicación estará disponible en `http://127.0.0.1:5000/`. Abre esta URL en tu navegador web para usar la aplicación.

## Uso

1. En la página principal podrás ver una lista de registros.

2. Puedes agregar, editar o eliminar registros usando los botones correspondientes.

3. La aplicación interactúa directamente con el archivo datos.csv para almacenar los registros.

## Estructura del Proyecto

- app.py: Archivo principal que contiene la configuración de la aplicación Flask y las rutas.
- templates/: Carpeta que contiene las plantillas HTML para las vistas.
- static/: Carpeta para los archivos estáticos como CSS o JavaScript.
- data/datos.csv: Archivo CSV donde se almacenan los registros de las personas.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas agregar nuevas características, resolver problemas o mejorar la aplicación, siéntete libre de crear un pull request.

## Autor

Esta aplicación fue desarrollada por [Luis Ares](https://github.com/luisaap-dev).

## Licencia

Este proyecto está bajo la Licencia [MIT](LICENSE). Puedes obtener más información en el archivo `LICENSE`.
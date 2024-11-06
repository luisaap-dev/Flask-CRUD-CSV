from flask import Flask, render_template, request, redirect, abort
from models import CSVModel

app = Flask(__name__)
csv_model = CSVModel()

PAGE_SIZE = 10

@app.route('/')
def index():
    _page = obtener_pagina_actual()
    data = csv_model.obtener_todos_los_datos()
    num_pages = calcular_numero_de_paginas(len(data))
    _page = limitar_pagina(_page, num_pages)
    pages = generar_rango_paginas(_page, num_pages)
    paginated_data = data[(_page - 1) * PAGE_SIZE: _page * PAGE_SIZE]
    
    return render_template('index.html', data=paginated_data, pages=pages, _page=_page, num_pages=num_pages)

@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        try:
            data = obtener_datos_formulario(request.form)
            csv_model.agregar_datos(data)
            return redirect('/')
        except KeyError:
            abort(400, "Formulario incompleto o inválido")
    return render_template('agregar.html')

@app.route('/editar/<id>', methods=['GET', 'POST'])
def editar(id):
    if request.method == 'POST':
        try:
            data = obtener_datos_formulario(request.form)
            if csv_model.actualizar_datos(id, data):
                return redirect('/')
            else:
                abort(404, "Registro no encontrado")
        except KeyError:
            abort(400, "Formulario incompleto o inválido")
    
    data = csv_model.obtener_datos(id)
    if not data:
        abort(404, "Datos no encontrados")
    return render_template('editar.html', data=data)

@app.route('/eliminar/<id>', methods=['POST'])
def eliminar(id):
    if csv_model.eliminar_datos(id):
        return redirect('/')
    abort(404, "Datos no encontrados")

@app.route('/mostrar/<id>')
def ver(id):
    data = csv_model.obtener_datos(id)
    if not data:
        abort(404, "Datos no encontrados")
    return render_template('mostrar.html', data=data)

def obtener_datos_formulario(formulario):
    """Obtiene y limpia los datos del formulario."""
    return {
        'nombre': limpiar_dato(formulario.get('nombre')),
        'apellidos': limpiar_dato(formulario.get('apellidos')),
        'email': limpiar_dato(formulario.get('email')),
        'telefono': limpiar_dato(formulario.get('telefono')),
        'sexo': limpiar_dato(formulario.get('sexo')),
        'direccion': limpiar_dato(formulario.get('direccion')),
        'ciudad': limpiar_dato(formulario.get('ciudad')),
        'pais': limpiar_dato(formulario.get('pais'))
    }

def limpiar_dato(dato):
    """Elimina espacios extra y devuelve el dato limpio."""
    return dato.strip() if dato else ''

def obtener_pagina_actual():
    """Obtiene el número de la página actual de la solicitud."""
    return int(request.args.get('_page', 1))

def calcular_numero_de_paginas(total_items):
    """Calcula el número total de páginas necesarias."""
    return (total_items + PAGE_SIZE - 1) // PAGE_SIZE

def limitar_pagina(pagina, num_paginas):
    """Limita la página al rango válido de páginas."""
    return max(1, min(pagina, num_paginas))

def generar_rango_paginas(pagina_actual, num_paginas):
    """Genera el rango de páginas para la paginación."""
    return range(max(1, pagina_actual - 2), min(num_paginas + 1, pagina_actual + 3))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

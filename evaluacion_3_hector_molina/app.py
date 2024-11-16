from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Ejercicio_1', methods=['GET', 'POST'])
def ejercicio_1():
    promedio = None
    estado = None
    error = None

    if request.method == 'POST':
        try:
            nota1 = float(request.form['nota1'])
            nota2 = float(request.form['nota2'])
            nota3 = float(request.form['nota3'])
            asistencia = float(request.form['asistencia'])

            promedio = (nota1 + nota2 + nota3) / 3

            if promedio >= 40 and asistencia >= 75:
                estado = "Aprobado"
            else:
                estado = "Reprobado"

        except ValueError:
            error = "Error: Por favor, ingresa valores válidos."

    return render_template('Ejercicio_1.html', promedio=promedio, estado=estado, error=error)

@app.route('/Ejercicio_2', methods=['GET', 'POST'])
def ejercicio_2():
    nombre_mas_largo = None
    longitud = None
    error = None

    if request.method == 'POST':
        try:
            nombres = [
                request.form['nombre1'],
                request.form['nombre2'],
                request.form['nombre3']
            ]

            nombre_mas_largo = max(nombres, key=len)
            longitud = len(nombre_mas_largo)

        except Exception:
            error = "Error: Por favor, ingresa valores válidos."

    return render_template('Ejercicio_2.html', nombre_mas_largo=nombre_mas_largo, longitud=longitud, error=error)

if __name__ == '__main__':
    app.run(debug=True)

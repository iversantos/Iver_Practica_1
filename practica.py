from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'clave_secreta_para_flash'

@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

@app.route('/quienes_somos')
def quienes_somos():
    return render_template('quienes_somos.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

@app.route('/noticias')
def noticias():
    return render_template('noticias.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    mensaje = None
    nombre = None

    if request.method == 'POST':
      
        nombre = request.form['nombre']
        email = request.form['email']
        mensaje_usuario = request.form['mensaje']

        if not nombre or not email or not mensaje_usuario:
            mensaje = 'Todos los campos son obligatorios'
        else:
            mensaje = f"Gracias {nombre}, hemos recibido tu mensaje."

    return render_template('contacto.html', mensaje=mensaje, nombre=nombre)

if __name__ == '__main__':
    app.run(debug=True)
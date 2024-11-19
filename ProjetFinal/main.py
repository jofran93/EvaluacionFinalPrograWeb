from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta para la página principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para el Ejercicio 1 (Cálculo de compras)
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])
        precio_por_tarro = 9000
        total_sin_descuento = cantidad * precio_por_tarro

        # Calcular el descuento
        if 18 <= edad <= 30:
            descuento = total_sin_descuento * 0.15
        elif edad > 30:
            descuento = total_sin_descuento * 0.25
        else:
            descuento = 0

        total_con_descuento = total_sin_descuento - descuento

        return render_template('ejercicio1.html',
                               nombre=nombre,
                               total_sin_descuento=total_sin_descuento,
                               descuento=descuento,
                               total_con_descuento=total_con_descuento)

    return render_template('ejercicio1.html')

# Ruta para el Ejercicio 2 (Inicio de sesión)
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']

        if usuario == 'juan' and contrasena == 'admin':
            mensaje = f"Bienvenido Administrador {usuario}"
        elif usuario == 'pepe' and contrasena == 'user':
            mensaje = f"Bienvenido Usuario {usuario}"
        else:
            mensaje = "Usuario o contraseña incorrectos"

        return render_template('ejercicio2.html', mensaje=mensaje)

    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)

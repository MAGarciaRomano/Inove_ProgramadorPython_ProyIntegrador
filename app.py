'''
Aplicación de ClienteVIP
------------------------
Curso Programador Python Inove
Proyecto Integrador
Autor: Martín A. García Romano
Año: 2022
Cliente V.I.P.
'''

import traceback
from datetime import date, datetime

from dateutil.relativedelta import relativedelta
from flask import (Flask, Response, jsonify, redirect, render_template,
                   request, url_for)

import clientevip

# Creación del servidor en FLask.
app = Flask(__name__)

# Ubicación de la base de datos que lee la app.
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///clientevip.db"

# Asociación del controlador de la base de datos con la aplicación.
clientevip.db.init_app(app)

# Ruta que se ingresa por la URL 127.0.0.1:5000
@app.route("/")
def index():
    try:
        # Imprimir los distintos endpoints disponibles.
        # Renderizado del template HTML index.html
        print("Renderizado de index.html")
        return render_template('index.html')
    except:
        return jsonify({'trace': traceback.format_exc()})


# Ruta que se ingresa por la URL 127.0.0.1:5000/registro.
@app.route("/registro", methods=['GET', 'POST'])
def registro():
    if request.method == 'GET':
        # Si el ingreso fue por el método GET es porque se acaba de cargar la página.
        try:
            # Renderizado del template HTML registro.html
            print("Renderizado de registro.html")
            return render_template('registro.html')
        except:
            return jsonify({'trace': traceback.format_exc()})

    if request.method == 'POST':
        try:
            # Obtener del HTTP POST JSON los datos del responsable y del cliente canino.
            # Datos del cliente canino:
            
            nombre_canino = str(request.form.get('nombre_canino')).title()
            print("Nombre:", nombre_canino)
            fecha_nacimiento = str(request.form.get('fecha_nacimiento'))
                        
            # Cálculo de la edad del canino en años, meses y días.
            fecha_nac = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
            print("Fecha de nacimiento:", fecha_nac.strftime("%d/%m/%Y"))
            edad = relativedelta(datetime.now(), fecha_nac)
            edad_canino = f"{edad.years} a, {edad.months} m, {edad.days} d"
            print("Edad:", edad_canino)
            
            raza = str(request.form.get('raza')).title()
            print("Raza:", raza)
            peso = str(request.form.get('peso'))
            print("Peso (kg):", peso)
            sexo = str(request.form.get('sexo')).capitalize()
            print("Sexo (Macho o Hembra):", sexo)
            esterilizado = str(request.form.get('esterilizado')).capitalize()
            print("Esterilizado(Si o No):", esterilizado)
            
            # ¡ATENCIÓN! Datos biomédicos comentados.
            #moquillo = str(request.form.get('fecha_moquillo'))
            #hepatitis = str(request.form.get('fecha_hepatitis'))
            #parvovirus = str(request.form.get('fecha_parvovirus'))
            #quintuple = str(request.form.get('fecha_quintuple'))
            #rabia = str(request.form.get('fecha_rabia'))
            #desparasitado_interno = str(request.form.get('fecha_desp_interno'))
            #desparasitado_externo = str(request.form.get('fecha_desp_externo'))

            moquillo = " "
            hepatitis = " "
            parvovirus = " "
            quintuple = " "
            rabia = " "
            desparasitado_interno = " "
            desparasitado_externo = " "
            
            # Datos del responsable:
            dni_responsable = str(request.form.get('dni_responsable'))
            print("DNI:", dni_responsable)
            apellido_responsable = str(request.form.get('apellido_responsable')).title()
            nombre_responsable = str(request.form.get('nombre_responsable')).title()
            
            # Compone apellido/s y nombre/s del responsable.
            apellido_y_nombre = str(apellido_responsable + '; ' + nombre_responsable)
            print("Apellido/s y Nombre/s:", apellido_y_nombre)
            
            calle_y_numero = str(request.form.get('calle_y_numero')).title()
            print("Calle y número:", calle_y_numero)
            localidad = str(request.form.get('localidad')).title()
            print("Localidad:", localidad)
            provincia = str(request.form.get('provincia')).title()
            print("Provincia:", provincia)
            telefono = str(request.form.get('telefono'))
            print("Teléfono (código de área + número):", telefono)
            
            # ¡ATENCIÓN! Falta armar la verificación de los datos introducidos.

            # Registro del nuevo cliente.
            print("Registrar al cliente", nombre_canino, "de", apellido_y_nombre,
                "DNI", dni_responsable)
            clientevip.insert(nombre_canino, fecha_nacimiento, edad_canino, raza, peso,
                            sexo, esterilizado, moquillo, hepatitis, parvovirus, quintuple,
                            rabia, desparasitado_interno, desparasitado_externo, dni_responsable,
                            apellido_y_nombre, calle_y_numero, localidad, provincia, telefono)
            return redirect(url_for('index'))
        except:
            return jsonify({'trace': traceback.format_exc()})


# Ruta que se ingresa por la URL 127.0.0.1:5000/consulta_nombre_dni
@app.route("/consulta_nombre_dni", methods=['GET', 'POST'])
def consulta_nombre_dni():
    if request.method == 'GET':
        # Si el ingreso fue por el método GET es porque se acaba de cargar la página.
        try:
            # Renderizado del template HTML consulta_nombre_dni.html
            print("Renderizado de consulta_nombre_dni.html")
            return render_template('consulta_nombre_dni.html')
        except:
            return jsonify({'trace': traceback.format_exc()})

    if request.method == 'POST':
        try:
            cons_nombre_canino = str(request.form.get('nombre_canino')).title()
            print("Nombre:", cons_nombre_canino)
            cons_dni_responsable = str(request.form.get('dni_responsable'))
            print("DNI:", cons_dni_responsable)

            print("Consultar por el cliente", cons_nombre_canino, "del responsable de DNI", cons_dni_responsable)
            
            reporte = clientevip.consulta_nombre_dni(cons_nombre_canino, cons_dni_responsable)
            return render_template('reporte_nombre_dni.html', reporte=reporte)
            
            
        except:
            return jsonify({'trace': traceback.format_exc()})

# Ruta que se ingresa por la URL 127.0.0.1:5000/consulta_nombre_dni/reporte_nombre_dni
@app.route("/consulta_nombre_dni/reporte_nombre_dni")


# Este método se ejecutará solo una vez la primera vez que se ingresa a un endpoint.
@app.before_first_request
def before_first_request_func():
    # Crear aquí todas las bases de datos.
    clientevip.db.create_all()
    print("Base de datos clientevip generada.")

if __name__ == '__main__':
    print('ClienteVIP@Server start!')

    # Lanzar servidor.
    app.run(host="127.0.0.1", port=5000)
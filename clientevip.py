'''
Administrador BD de ClienteVIP
------------------------------
Curso Programador Python Inove
Proyecto Integrador
Autor: Martín A. García Romano
Año: 2022
Cliente V.I.P.
'''

from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Float, String
db = SQLAlchemy()

# NOTA: Por un bug en el linter de Visual verán problemas con
# el tipo de dato "db". No le den importancia.

# Creación del a tabla Cliente de la Base de Datos cliente_vip.db
class Cliente(db.Model):
    __tablename__ = "cliente"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre_canino = db.Column(db.String)
    fecha_nacimiento = db.Column(db.String)
    edad = db.Column(db.String)
    raza = db.Column(db.String)
    peso = db.Column(db.String)
    sexo = db.Column(db.String)
    esterilizado = db.Column(db.String)
    moquillo = db.Column(db.String, nullable=True)
    hepatitis = db.Column(db.String, nullable=True)
    parvovirus = db.Column(db.String, nullable=True)
    quintuple = db.Column(db.String, nullable=True)
    rabia = db.Column(db.String, nullable=True)
    desparasitado_interno = db.Column(db.String, nullable=True)
    desparasitado_externo = db.Column(db.String, nullable=True)
    dni_responsable = db.Column(db.String)
    apellido_y_nombre = db.Column(db.String)
    calle_y_numero = db.Column(db.String)
    localidad = db.Column(db.String)
    provincia = db.Column(db.String)
    telefono = db.Column(db.String)

    def __repr__(self):
        return f"Nombre {self.nombre_canino}, nacido {self.fecha_nacimiento}, responsable {self.apellido_y_nombre}, telefono {self.telefono}"

def insert(nombre_canino, fecha_nacimiento, edad_canino, raza, peso, sexo, esterilizado, moquillo,
        hepatitis, parvovirus, quintuple, rabia, desparasitado_interno, desparasitado_externo, dni_responsable,
        apellido_y_nombre, calle_y_numero, localidad, provincia, telefono):
    # Crear un nuevo registro de reponsable humano.
    nuevo_cliente = Cliente(nombre_canino=nombre_canino,
                            fecha_nacimiento=fecha_nacimiento,
                            edad=edad_canino,
                            raza=raza,
                            peso=peso, 
                            sexo=sexo,
                            esterilizado=esterilizado,
                            moquillo=moquillo,
                            hepatitis=hepatitis,
                            parvovirus=parvovirus,
                            quintuple=quintuple,
                            rabia=rabia,
                            desparasitado_interno=desparasitado_interno,
                            desparasitado_externo=desparasitado_externo,
                            dni_responsable=dni_responsable,
                            apellido_y_nombre=apellido_y_nombre,
                            calle_y_numero=calle_y_numero,
                            localidad=localidad,
                            provincia=provincia,
                            telefono=telefono)
    
    # Agregar el registro del nuevo responsable a la BD.
    db.session.add(nuevo_cliente)
    db.session.commit()


# Función que realiza consulta por nombre del canino y dni del responsable.
def consulta_nombre_dni(nombre_canino, dni_responsable):
    
    query = db.session.query(Cliente).filter((Cliente.nombre_canino==nombre_canino)&(Cliente.dni_responsable==dni_responsable))
    
    #if limit>0:
    #    query = query.limit(limit)
    #    if offset > 0:
    #        query = query.offset(offset)

    json_consulta_lista =[]
    
    for resultado in query:
        json_resultado = {'nombre_canino': resultado.nombre_canino,
                        'fecha_nacimiento': resultado.fecha_nacimiento,
                        'raza': resultado.raza,
                        'peso': resultado.peso,
                        'sexo': resultado.sexo,
                        'esterilizado': resultado.esterilizado,
                        'moquillo': resultado.moquillo,
                        'hepatitis': resultado.hepatitis,
                        'parvovirus': resultado.parvovirus,
                        'quintuple': resultado.quintuple,
                        'rabia': resultado.rabia,
                        'desparasitado_interno': resultado.desparasitado_interno,
                        'desparasitado_externo': resultado.desparasitado_externo,
                        'dni_respnsable': resultado.dni_responsable,
                        'apellido_y_nombre': resultado.apellido_y_nombre,
                        'telefono':resultado.telefono}
        
        print(json_resultado)
        json_consulta_lista.append(json_resultado)
        
    return json_consulta_lista

# Test.
# Acá tomé como modelo el test que propusieron en los ejercicios de práctica.

#if __name__ == "__main__":
#    print("Test del modulo clientevip.py")

    # Crear una aplicación Flask para testing
    # y una base de datos fantasma (auxiliar o dummy)
    # Referencia:
    # https://stackoverflow.com/questions/17791571/how-can-i-test-a-flask-application-which-uses-sqlalchemy
#    app = Flask(__name__)
#    app.config['TESTING'] = True
#    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///testclientevip.db"
    # Bindear la DB con nuestra app Flask
#    db.init_app(app)
#    app.app_context().push()

#    db.create_all()

    # Aquí se puede ensayar todo lo que necesitemos con nuestra DB

    # Test "insert"
    # Generamos datos inventados y probamos si funciona correctamente
    # la función insert
    #insert(time=datetime.now(), name="Inove", heartrate=70)

    # Test "report"
    # Ahora que nuestra base de datos tiene datos, podemos probar
    # las funciones que acceden a esos datos y ver si funcionan correctamente
    #datos = report()
    #print(datos)

    #db.session.remove()
    #db.drop_all()
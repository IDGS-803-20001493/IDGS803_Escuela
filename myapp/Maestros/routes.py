from flask import Blueprint

maestros = Blueprint('maestros',__name__)

from db import get_connection

from flask import Flask, redirect, render_template
from flask import request
from flask_wtf.csrf import CSRFProtect

@maestros.route('/consultaMaestros', methods=['GET','POST'])
def consultaMaestros():
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('call consultarMaestros()')
            resultset = cursor.fetchall()
        connection.close()
        print(resultset)
        
        return render_template('FormularioMaestros.html', resultado = resultset, ID = "", Nombre = "", Apellido = "", email = "")
    except Exception as ex: 
        print(ex)

@maestros.route('/insertarMaestro', methods=['GET','POST'])
def insertarMaestro():
    try:
        ID = (request.form.get('ID'))
        Nombre = (request.form.get('Nombre'))
        Apellido = (request.form.get('Apellido'))
        email = (request.form.get('email'))
        print (len(ID))
        connection = get_connection()
        with connection.cursor() as cursor:

            if len(ID) == 0:
                cursor.execute('call insertarMaestros(%s,%s,%s)',
                                (Nombre,Apellido,email))
            else:
                cursor.execute('call actualizarMaestros(%s,%s,%s,%s)',
                           (ID,Nombre,Apellido,email))
        connection.commit()
        connection.close()
        
        return render_template('FormularioMaestros.html')
    except Exception as ex: 
        print(ex)



@maestros.route('/eliminarMaestro', methods=['GET','POST'])
def eliminarMaestro():
    try:
        ID=request.args.get('ID')

        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('call deleteMaestros(%s)',
                           (ID))
        connection.commit()
        connection.close()
        
        return render_template('FormularioMaestros.html')
    except Exception as ex: 
        print(ex)
        
@maestros.route('/cargarDatos2', methods=['GET','POST'])
def cargarDatos2():

    ID = request.args.get('ID')
    Nombre = request.args.get('Nombre')
    Apellido = request.args.get('Apellido')
    email = request.args.get('email')
    
    return render_template('FormularioMaestros.html', ID = ID, Nombre = Nombre, Apellido = Apellido, email = email)
from flask import Blueprint
from db import get_connection

from flask import Flask, redirect, render_template
from flask import request
from flask import url_for
import forms

from flask import jsonify
from flask_wtf.csrf import CSRFProtect

alumnos = Blueprint('alumnos',__name__)


@alumnos.route('/consultaAlumnos', methods=['GET','POST'])
def consultaAlumnos():
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('call consultarAlumnos()')
            resultset = cursor.fetchall()
        connection.close()
        print(resultset)
        
        return render_template('FormularioAlumnos.html', resultado = resultset, ID = "", Nombre = "", Apellido = "", email = "")
    except Exception as ex: 
        print(ex)

@alumnos.route('/insertarAlumno', methods=['GET','POST'])
def insertarAlumno():
    try:
        ID = (request.form.get('ID'))
        Nombre = (request.form.get('Nombre'))
        Apellido = (request.form.get('Apellido'))
        email = (request.form.get('email'))
        print (len(ID))
        connection = get_connection()
        with connection.cursor() as cursor:

            if len(ID) == 0:
                cursor.execute('call insertarAlumnos(%s,%s,%s)',
                                (Nombre,Apellido,email))
            else:
                cursor.execute('call actualizarAlumnos(%s,%s,%s,%s)',
                           (ID,Nombre,Apellido,email))
        connection.commit()
        connection.close()
        
        return render_template('FormularioAlumnos.html')
    except Exception as ex: 
        print(ex)



@alumnos.route('/eliminarAlumno', methods=['GET','POST'])
def eliminarAlumno():
    try:
        ID=request.args.get('ID')

        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('call deleteAlumnos(%s)',
                           (ID))
        connection.commit()
        connection.close()
        
        return render_template('FormularioAlumnos.html')
    except Exception as ex: 
        print(ex)
        
@alumnos.route('/cargarDatos', methods=['GET','POST'])
def cargarDatos():

    ID = request.args.get('ID')
    Nombre = request.args.get('Nombre')
    Apellido = request.args.get('Apellido')
    email = request.args.get('email')
    
    return render_template('FormularioAlumnos.html', ID = ID, Nombre = Nombre, Apellido = Apellido, email = email)
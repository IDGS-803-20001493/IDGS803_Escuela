import flask

from Alumnos.routes import alumnos
from Maestros.routes import maestros
from flask import Blueprint
from db import get_connection

from flask import Flask, redirect, render_template
from flask import request
from flask import url_for
import forms
from models import db
from models import Alumnos

from flask import jsonify
from flask_wtf.csrf import CSRFProtect


from config import DevelopmentConfig

app = flask.Flask(__name__)
app.config['DEBUG']=True
app.config['SECRET_KEY']="Esta es la clave encriptada"
csrf = CSRFProtect()

app.config.from_object(DevelopmentConfig)


@app.route("/", methods=['GET'])
def home():
    return render_template('index.html')

app.register_blueprint(alumnos)
app.register_blueprint(maestros)

if __name__=='__main__':
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=3000)

    
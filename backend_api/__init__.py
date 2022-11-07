#criar app
from flask import Flask
from flask_restful import Api #PARA A API
from flask_sqlalchemy import SQLAlchemy #para o banco de dados
from flask_migrate import Migrate #para o bando de dados
from flask_marshmallow import Marshmallow #para o schema

#instancia do flask 
app = Flask(__name__)

#importando configurações do projeto -> config.py
app.config.from_object('config')


#instancias para o banco de dados
#instancia do SQLAlchemy
db = SQLAlchemy(app)

#Instancia do marshmallow
ma = Marshmallow(app)

migrate = Migrate(app, db)

#instancia da api
api = Api(app)


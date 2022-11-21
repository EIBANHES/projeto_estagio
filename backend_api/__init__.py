from flask import Flask
from flask_restful import Api               # para a API
from flask_sqlalchemy import SQLAlchemy     # para o banco de dados
from flask_migrate import Migrate           # para o banco de dados
from flask_marshmallow import Marshmallow   # para o schema


# instancia do flask
app = Flask(__name__)
# importando configurações do arquivo config.py da raiz
app.config.from_object('config')    

# Instancias para o banco de dados
db = SQLAlchemy(app)
ma = Marshmallow(app)

migrate = Migrate(app, db)

# intância da API
api = Api(app)

# para detectar no migrate
from .models import estagiario_origem_model
from .views import estagiario_origem_view

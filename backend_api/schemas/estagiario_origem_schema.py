#validação dos dados do model
from backend_api import ma
from backend_api.models import estagiario_origem_model
from marshmallow import fields

class EstagiarioOrigemSchema(ma.SQLAlchemyAutoSchema):
    class Meta: #nome padrao do framework, tem que ser esse pois vai sobreescrever
        model = estagiario_origem_model.EstagiarioOrigem 
        load_instance = True; #fica validando
        fields = ('id', 'origem') #dados que serao retornados
        
        #nao precisa passar id pq é autoincrement
        origem = fields.String(required=True) 
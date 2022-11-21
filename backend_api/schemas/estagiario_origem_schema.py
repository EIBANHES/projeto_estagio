from backend_api import ma
from ..models import estagiario_origem_model
from marshmallow import fields


class EstagiarioOrigemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:     # nome padrão do framework, tem que ser esse pois vai sobrescrever
        model = estagiario_origem_model.EstagiarioOrigem
        load_instance = True    # recarregamento
        fields = ('id', 'origem')
    
    # aqui não precisa passar o ID porque ele é auto increment
    origem = fields.String(required=True)


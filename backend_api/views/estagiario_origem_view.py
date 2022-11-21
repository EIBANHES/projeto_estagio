from flask_restful import Resource      # Resouce vai prover recursos, como: Criar, Editar, Listar, etc 
from backend_api import api
from ..schemas import estagiario_origem_schema
from ..entidades import estagiario_origem_entidade
from ..services import estagiario_origem_service 
'''
requesct - requisicoes
make_response - serve p/ tratar o que vem das requisiçoes
jsonify - converter os valores em json
'''
from flask import request, make_response, jsonify


class EstagiarioOrigemNoId(Resource):
    def get(self):
        estagiario_origem = estagiario_origem_service.listar_estagiario_origem()
        eo_schema = estagiario_origem_schema.EstagiarioOrigemSchema(many=True)      # many - todos os registros

        x = eo_schema.jsonify(estagiario_origem)

        return make_response(x, 200)


    def post(self):
        # validar no schema
        eo_schema = estagiario_origem_schema.EstagiarioOrigemSchema()
        validate = eo_schema.validate(request.json)         # passando uma requisição json para validar no schema

        if validate:                                        # se houver erro de validacao
            return make_response(jsonify(validate), 400)   
        else:
            origem = request.json["origem"]

            # entidade
            nova_origem = estagiario_origem_entidade.EstagiarioOrigem(origem=origem)

            # service
            resultado = estagiario_origem_service.cadastrar_estagiario_origem(nova_origem)

            x = eo_schema.jsonify(resultado)
            return make_response(x, 201)        


class EstagiarioOrigemWithId(Resource):
    def get(self, id):
        pass


    def put(self, id):
        pass


    def delete(self, id):
        pass


# rota -  Recurso sem passar id
api.add_resource(EstagiarioOrigemNoId, '/estagiario_origem')

api.add_resource(EstagiarioOrigemWithId, '/estagiario_origem/<int:id>')
from backend_api.entidades import estagiario_origem_entidade
from ..models import estagiario_origem_model
from backend_api import db


def cadastrar_estagiario_origem(estagiario_origem):
    estagiario_origem_db = estagiario_origem_model.EstagiarioOrigem(
        origem = estagiario_origem.origem
    )
    db.session.add(estagiario_origem_db)
    db.session.commit()
    return estagiario_origem_db


def listar_estagiario_origem():
    # faz referencia ao modelo e executando uma query para buscar todos os registros
    estagiario_origem = estagiario_origem_model.EstagiarioOrigem.query.all()
    return estagiario_origem


def listar_estagiario_origem_por_id():
    pass
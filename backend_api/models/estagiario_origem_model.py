from backend_api import db


class EstagiarioOrigem(db.Model): #herda da clase do db
    #nome da tabela no banco
    __tablename__ = 'estagiario_origem'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False) #nullable = a not null
    origem = db.Column(db.String(20), nullable=False)
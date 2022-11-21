from backend_api import db


class EstagiarioOrigem(db.Model):
    __tablename__ = 'estagiario_origem'     # nome da tabela no banco
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    origem = db.Column(db.String(20), nullable=False)




#-- estagiario_origem
#CREATE TABLE estagiario_origem (
#	id 						INT PRIMARY KEY AUTO_INCREMENT 	NOT NULL,
#	origem					VARCHAR(20)					    NOT NULL
#);


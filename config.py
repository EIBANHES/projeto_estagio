# flask
DEBUG = True

#Configs banco de dados
USERNAME = 'root'
PASSWORD = ''
SERVER = 'localhost'
DATABASE = 'sistema_controle_estagiario'

SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DATABASE}'

DEBUG = True

# Configurações do banco de dados
USERNAME = 'root'
PASSWORD = ''
SERVER = 'localhost'
DATABASE = 'sistema_controle_estagiarios'

SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DATABASE}'
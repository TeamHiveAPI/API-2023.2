#variaveis universais para configurações
SECRET_KEY = 'timehive'

SQLALCHEMY_DATABASE_URI = \
 '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
     SGBD = 'mysql+mysqlconnector',
     usuario = 'fatec',
     senha = 'senha',
     servidor = 'localhost:3306', 
     database = 'bd'
 )
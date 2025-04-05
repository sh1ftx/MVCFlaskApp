from flask import Flask

# Cria a instância principal do Flask
app = Flask(__name__)

# Importa as rotas
from App import routes
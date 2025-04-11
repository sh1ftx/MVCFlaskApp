from flask import Flask

# Cria o app do Flask
app = Flask(__name__)

# Importa as rotas
from App import views
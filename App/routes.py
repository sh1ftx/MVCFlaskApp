from flask import request, jsonify, render_template
from App.crud import * 
from App import app 

# Apenas para renderizar a primeira pagina do site
@app.route("/")
def home():
    return render_template("index.html")

#Função para adicionar o usuario ao banco de dados
@app.route("/cadastro", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        data = request.json

        user_data = {
            "nome": data.get("nome"),
            "telefone": data.get("telefone"),
            "email": data.get("email"),
            "cidade": data.get("cidade"),
            "data_nascimento": data.get("data_nascimento")
        }
        
        create("usuarios", user_data)
        
        return jsonify({"message": "Usuário cadastrado com sucesso!"}), 201
    else:
        return render_template("page_cadastro.html")
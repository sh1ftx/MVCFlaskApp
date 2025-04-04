from flask import request, jsonify, render_template
# from app.models import database
#presumindo que o gleisun vai fazer algo pra retornar o banco

#db = funcao de conexao com o database

#Função para adicionar o usuario ao banco de dados
@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        dados = request.json
        cursor = db.cursor()

        #Inserção do usuario ao database
        cursor.execute(
            "INSERT INTO usuarios (nome, email, telefone, cidade, data_nascimento) VALUES (%s, %s, %s, %s, %s)",
            (dados.get("nome"), 
             dados.get("email"),
             dados.get("telefone"),
             dados.get("cidade"),
             dados.get("data_nascimento"))
        )
        db.commit()
        cursor.close()
        
        return jsonify({"message": "Usuário cadastrado com sucesso!"}), 201
    else:
        return render_template("page-cadastro.html")
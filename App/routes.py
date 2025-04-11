from flask import request, jsonify, render_template, redirect, url_for
from App.crud import * 
from App import app 

# Apenas para renderizar a primeira pagina do site
@app.route("/")
def home():
    return render_template("index.html")

# Função para adicionar o usuario ao banco de dados
@app.route("/user_register", methods=["GET", "POST"])
def user_register():
    if request.method == "POST":
        
        data = request.json
        email = data.get("email")
        
        # Verifica se o email ja ta em uso
        email_used = read("usuarios", f"email = '{email}'")
        if email_used:
            return jsonify({"error": "Email em uso"}), 409

        user_data = {
            "nome": data.get("nome"),
            "telefone": data.get("telefone"),
            "email": data.get("email"),
            "cidade": data.get("cidade"),
            "data_nascimento": data.get("data_nascimento")
        }
        
        create("usuarios", user_data)
        
        return jsonify({"message": "Usuário cadastrado com sucesso!"}), 201 # msg de sucesso
    else:
        return render_template("user_register.html")
    
# Função que renderiza a pagina de edição e permite as alterações    
@app.route("/edit_user/<int:id>", methods=["GET", "POST"])
def edit_user(id):
    if request.method == "POST":
        data = request.json
        email = data.get("email")

        # Verifica se o email ja ta em uso
        email_used = read("usuarios", f"email = '{email}'")
        if email_used:
            return jsonify({"error": "Email em uso"}), 409

        user_data = {
            "nome": data.get("nome"),
            "telefone": data.get("telefone"),
            "email": data.get("email"),
            "cidade": data.get("cidade"),
            "data_nascimento": data.get("data_nascimento")
        }

        update("usuarios", user_data, f"id = {id}")
        return jsonify({"message": "Usuário atualizado com sucesso!"}), 200
    
    return render_template("edit_user.html", user=read("usuarios", f"id = {id}")[0])


# Função que renderiza a pagina que mostra todos os usuarios
@app.route("/user_list")
def user_list():
    return render_template("user_list.html", users = read("usuarios"))

# Função para excluir um usuario
@app.route("/excluir/<int:id>")
def delete_user(id):
    delete("usuarios", f"id = {id}")
    return redirect(url_for("user_list"))

# ------- Funções referentes a tabela de produtos

# Página de cadastro de produto
@app.route("/register_product", methods=["GET", "POST"])
def register_product():
    if request.method == "POST":
        data = request.json
        produto = {
            "nome": data.get("nome"),
            "marca": data.get("marca"),
            "preco": data.get("preco"),
            "estoque": data.get("estoque")
        }
        create("produtos", produto)
        return jsonify({"message": "Produto cadastrado com sucesso!"}), 201
    return render_template("register_product.html")

# Página de listagem de produtos
@app.route("/product_list")
def product_list():
    return render_template("product_list.html", produtos = read("produtos"))

# Editar produto
@app.route("/edit_product/<int:id>", methods=["GET", "POST"])
def edit_product(id):
    if request.method == "POST":
        data = request.json
        produto = {
            "nome": data.get("nome"),
            "marca": data.get("marca"),
            "preco": data.get("preco"),
            "estoque": data.get("estoque")
        }
        update("produtos", produto, f"id = {id}")
        return jsonify({"message": "Produto atualizado com sucesso!"}), 200

    return render_template("edit_product.html", produto = read("produtos", f"id = {id}")[0])

# Excluir produto
@app.route("/excluir_produto/<int:id>")
def excluir_produto(id):
    delete("produtos", f"id = {id}")
    return redirect(url_for("product_list"))

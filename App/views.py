from flask import request, jsonify, render_template, redirect, url_for
from App import app
from App.controllers import *

# rota para a pagina inicial
@app.route("/")
def home():
    return render_template("index.html")

# rota para o cadastro
@app.route("/user_register", methods=["GET", "POST"])
def user_register():
    if request.method == "POST":
        data = request.json
        response, status = add_new_user(data)
        return jsonify(response), status
    
    return render_template("user_register.html")

# rota de edicao
@app.route("/edit_user/<int:id>", methods=["GET", "PUT"])
def edit_user_route(id):
    if request.method == "PUT":
        data = request.json
        response, status = edit_user(id, data)
        return jsonify(response), status
    
    return render_template("edit_user.html", user=get_user(id))

# rota de exibicao de tds os usuarios
@app.route("/user_list")
def user_list_route():
    return render_template("user_list.html", users=list_users())

# rota de delete
@app.route("/delete_user/<int:id>", methods=["GET", "DELETE"])
def delete_user_route(id):
    delete_user(id)
    return redirect(url_for("user_list_route"))


# ---- Rotas referentes aos produtos ----

# registrar
@app.route("/register_product", methods=["GET", "POST"])
def registrar_produto_route():
    if request.method == "POST":
        data = request.json
        response, status = add_new_product(data)
        return jsonify(response), status
    return render_template("register_product.html")

# exibir tds
@app.route("/product_list")
def lista_produtos_route():
    return render_template("product_list.html", produtos=list_products())

# editar
@app.route("/edit_product/<int:id>", methods=["GET", "PUT"])
def editar_produto_route(id):
    if request.method == "PUT":
        data = request.json
        response, status = edit_product(id, data)
        return jsonify(response), status
    return render_template("edit_product.html", produto=get_product(id))

# deletar
@app.route("/excluir_produto/<int:id>", methods=["GET", "DELETE"])
def excluir_produto_route(id):
    delete_product(id)
    return redirect(url_for("lista_produtos_route"))
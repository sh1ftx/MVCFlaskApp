from App.crud import *

# adiciona usuario
def add_new_user(data):
    email = data.get("email")

    # verifica se o email ta disponivel
    email_used = read("usuarios", f"email = '{email}'")
    if email_used:
        return {"error": "Email em uso"}, 409

    user_data = {
        "nome": data.get("nome"),
        "telefone": data.get("telefone"),
        "email": data.get("email"),
        "cidade": data.get("cidade"),
        "data_nascimento": data.get("data_nascimento")
    }

    create("usuarios", user_data)
    return {"message": "Usuário cadastrado com sucesso!"}, 201


# edita as informacoes do usuario
def edit_user(id, data):
    email = data.get("email")

    # verifiaca email disponivel
    email_used = read("usuarios", f"email = '{email}' AND id != '{id}'")
    if email_used:
        return {"error": "Email em uso"}, 409

    user_data = {
        "nome": data.get("nome"),
        "telefone": data.get("telefone"),
        "email": data.get("email"),
        "cidade": data.get("cidade"),
        "data_nascimento": data.get("data_nascimento")
    }

    update("usuarios", user_data, f"id = {id}")
    return {"message": "Usuário atualizado com sucesso!"}, 200

# retorna todos os usuarios cadastrados
def list_users():
    return read("usuarios")

# retorna apenas um usuario especifico
def get_user(id):
    return read("usuarios", f"id = {id}")[0]

# deleta um usuario
def delete_user(id):
    delete("usuarios", f"id = {id}")

# ------ Funcoes referentes aos produtos -------

# adiciona produto
def add_new_product(data):
    produto = {
        "nome": data.get("nome"),
        "marca": data.get("marca"),
        "preco": data.get("preco"),
        "estoque": data.get("estoque")
    }
    create("produtos", produto)
    return {"message": "Produto cadastrado com sucesso!"}, 201

# edita
def edit_product(id, data):
    produto = {
        "nome": data.get("nome"),
        "marca": data.get("marca"),
        "preco": data.get("preco"),
        "estoque": data.get("estoque")
    }
    update("produtos", produto, f"id = {id}")
    return {"message": "Produto atualizado com sucesso!"}, 200

# exibe todos
def list_products():
    return read("produtos")

# retorna um especifico
def get_product(id):
    return read("produtos", f"id = {id}")[0]

# deleta o produto
def delete_product(id):
    delete("produtos", f"id = {id}")

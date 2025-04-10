import sqlite3

#função para conectar no bando de dados
def conectar():
    conexao = sqlite3.connect('database_teste_mvc.db')
    return conexao

conexao = conectar()

cursor = conexao.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        telefone TEXT NOT NULL,
        cidade TEXT NOT NULL,
        data_nascimento DATETIME NOT NULL
    )""")


cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    marca TEXT NOT NULL,
                    preco TEXT NOT NULL,
                    estoque INTEGER NOT NULL)""")
                    
conexao.commit()

conexao.close()

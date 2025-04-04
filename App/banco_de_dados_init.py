import sqlite3

#função para conectar no bando de dados
def conectar():
    conexao = sqlite3.connect('database_mvc.db')
    return conexao

conexao = conectar()

cursor = conexao.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    idade INTEGER NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    teLefone TEXT NOT NULL,
                    cidade TEXT NOT NULL,
                    data_nascimento DATETIME NOT NULL)""")


cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    marca TEXT NOT NULL,
                    preco TEXT UNIQUE NOT NULL,
                    estoque INTEGER NOT NULL)""")
                    
conexao.commit()

conexao.close()

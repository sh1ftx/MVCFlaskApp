import sqlite3

banco = sqlite3.connect('database_mvc.db')
    
cursor = banco.cursor()

sql = """
CREATE TABLE usuarios(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL)"""


sql = """
CREATE TABLE produtos(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    marca TEXT NOT NULL,
                    preco TEXT UNIQUE NOT NULL)"""
                    
cursor.execute(sql)

banco.commit()

banco.close()

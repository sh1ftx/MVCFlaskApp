from banco_de_dados_init import conectar 
import sqlite3

#funçao para inserir dados na tabela
def create(tabela, dados):
    colunas = ', '.join(dados.keys())
    valores = tuple(dados.values())
    placeholders = ', '.join(['?'] * len(dados))

    sql = f"INSERT INTO {tabela} ({colunas}) VALUES ({placeholders})"

    conexao = conectar()  
    cursor = conexao.cursor()
    cursor.execute(sql, valores)
    conexao.commit()
    conexao.close()

#função para puxar dados das tabelas    
def read(tabela, condicao=None):
    conexao = conectar()
    cursor = conexao.cursor()

    if condicao:
        sql = f"SELECT * FROM {tabela} WHERE {condicao}"
    else:
        sql = f"SELECT * FROM {tabela}"

    cursor.execute(sql)
    resultados = cursor.fetchall()
    conexao.close()
    return resultados

#função para atualizar os dados
def update(tabela, dados, condicao):
    colunas = ', '.join([f"{chave}=?" for chave in dados.keys()])
    valores = tuple(dados.values())

    sql = f"UPDATE {tabela} SET {colunas} WHERE {condicao}"

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(sql, valores)
    conexao.commit()
    conexao.close()

#função para deletar dados
def delete(tabela, condicao):
    sql = f"DELETE FROM {tabela} WHERE {condicao}"

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(sql)
    conexao.commit()
    conexao.close()

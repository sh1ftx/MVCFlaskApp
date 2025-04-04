import sqlite3

def commit_close(*func):
   def decorator(*args): 
    banco = sqlite3.connect('database_mvc.db')
    cursor = banco.cursor()
    sql = func(*args)
    cursor.exeecute(sql)
    banco.commit()
    banco.close()
   return decorator 

@commit_close
def adicionar_usuarios(nome,phone,email):
    return """
    INSERT INTO usuarios(nome,phone,email)
    VALURES ('{}','{}','{})
    """.format(nome,phone,email)

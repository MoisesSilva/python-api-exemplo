from flask import g
import sqlite3

# Criando a conexão com BD
def connect_db():
    sql = sqlite3.connect('D:\cursos\Flask\python-api\members.db')
    sql.row_factory = sqlite3.Row
    return sql

# Retornando essa conexão
def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db
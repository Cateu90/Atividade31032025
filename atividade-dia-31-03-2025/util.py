from contextlib import contextmanager
import sqlite3

# Define o nome padrão do arquivo do banco de dados
DB_NAME = 'dados.db'

@contextmanager
def get_db_connection(db_name=DB_NAME):
    """
    Gerenciador de contexto para conexões com o banco de dados SQLite.
    Garante que a conexão seja fechada e as alterações commitadas.
    """
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS produtos (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, preco REAL NOT NULL, estoque INTEGER NOT NULL)")
        cursor.execute("CREATE TABLE IF NOT EXISTS comandas (id INTEGER PRIMARY KEY AUTOINCREMENT, numero INTEGER NOT NULL, data_abertura DATETIME NOT NULL, data_fechamento DATETIME, valor_total REAL NOT NULL DEFAULT 0.0)")
        cursor.execute("CREATE TABLE IF NOT EXISTS caixas (id INTEGER PRIMARY KEY AUTOINCREMENT, data_abertura DATETIME NOT NULL, data_fechamento DATETIME, valor_inicial REAL NOT NULL, valor_final REAL)")
        yield conn
    finally:
        if conn:
            conn.commit()
            conn.close()

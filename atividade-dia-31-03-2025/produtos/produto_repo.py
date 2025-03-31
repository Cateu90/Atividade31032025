from typing import List, Optional
from produtos.produto import Produto
from produtos import produto_sql as sql
from util import get_db_connection
import sqlite3

class ProdutoRepo:
    def __init__(self):
        self._criar_tabela()

    def _criar_tabela(self):
        try:
            with get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(sql.CREATE_TABLE)
        except sqlite3.Error as e:
            print(f"Erro ao criar tabela: {e}")

    def adicionar(self, produto: Produto) -> Optional[int]:
        try:
            with get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(sql.INSERT_PRODUTO, (produto.nome, produto.preco, produto.estoque))
                return cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Erro ao adicionar produto: {e}")
            return None

    def obter(self, produto_id: int) -> Optional[Produto]:
        try:
            with get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(sql.SELECT_PRODUTO, (produto_id,))
                row = cursor.fetchone()
                if row:
                    return Produto(id=row[0], nome=row[1], preco=row[2], estoque=row[3])
                return None
        except sqlite3.Error as e:
            print(f"Erro ao obter produto {produto_id}: {e}")
            return None

    def obter_todos(self) -> List[Produto]:
        try:
            with get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(sql.SELECT_TODOS_PRODUTOS)
                rows = cursor.fetchall()
                return [Produto(id=row[0], nome=row[1], preco=row[2], estoque=row[3]) for row in rows]
        except sqlite3.Error as e:
            print(f"Erro ao obter todos os produtos: {e}")
            return []

    def atualizar(self, produto: Produto) -> bool:
        if produto.id is None:
            print("Erro: Produto sem ID não pode ser atualizado.")
            return False
        try:
            with get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(sql.UPDATE_PRODUTO, (produto.nome, produto.preco, produto.estoque, produto.id))
                return cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Erro ao atualizar produto {produto.id}: {e}")
            return False

    def excluir(self, produto_id: int) -> bool:
        try:
            with get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(sql.DELETE_PRODUTO, (produto_id,))
                return cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Erro ao excluir produto {produto_id}: {e}")
            return False

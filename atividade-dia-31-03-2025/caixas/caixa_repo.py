from typing import List, Optional
from caixas.caixa import Caixa
from caixas import caixa_sql as sql
from util import get_db_connection
import sqlite3

class CaixaRepo:
    def __init__(self):
        self._criar_tabela()

    def _criar_tabela(self):
        try:
            with get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(sql.CREATE_TABLE)
        except sqlite3.Error as e:
            print(f"Erro ao criar tabela: {e}")

    def adicionar(self, caixa: Caixa) -> Optional[int]:
        try:
            with get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(sql.INSERT_CAIXA, (caixa.data_abertura, caixa.valor_inicial))
                return cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Erro ao adicionar caixa: {e}")
            return None

    def obter(self, caixa_id: int) -> Optional[Caixa]:
        try:
            with get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(sql.SELECT_CAIXA, (caixa_id,))
                row = cursor.fetchone()
                if row:
                    return Caixa(id=row[0], data_abertura=row[1], data_fechamento=row[2], valor_inicial=row[3], valor_final=row[4])
                return None
        except sqlite3.Error as e:
            print(f"Erro ao obter caixa {caixa_id}: {e}")
            return None

    def obter_todos(self) -> List[Caixa]:
        try:
            with get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(sql.SELECT_TODOS_CAIXAS)
                rows = cursor.fetchall()
                return [Caixa(id=row[0], data_abertura=row[1], data_fechamento=row[2], valor_inicial=row[3], valor_final=row[4]) for row in rows]
        except sqlite3.Error as e:
            print(f"Erro ao obter todos os caixas: {e}")
            return []

    def atualizar(self, caixa: Caixa) -> bool:
        if caixa.id is None:
            print("Erro: Caixa sem ID não pode ser atualizado.")
            return False
        try:
            with get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(sql.UPDATE_CAIXA, (caixa.data_abertura, caixa.data_fechamento, caixa.valor_inicial, caixa.valor_final, caixa.id))
                return cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Erro ao atualizar caixa {caixa.id}: {e}")
            return False

    def excluir(self, caixa_id: int) -> bool:
        try:
            with get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(sql.DELETE_CAIXA, (caixa_id,))
                return cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Erro ao excluir caixa {caixa_id}: {e}")
            return False

from typing import List, Optional
from comandas.comanda import Comanda
from comandas import comanda_sql as sql
from util import get_db_connection
import sqlite3

class ComandaRepo:
    def __init__(self):
        self._criar_tabela()

    def _criar_tabela(self):
        try:
            with get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(sql.CREATE_TABLE)
        except sqlite3.Error as e:
            print(f"Erro ao criar tabela: {e}")

    def adicionar(self, comanda: Comanda) -> Optional[int]:
        try:
            with get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(sql.INSERT_COMANDA, (comanda.numero, comanda.data_abertura))
                return cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Erro ao adicionar comanda: {e}")
            return None

    def obter(self, comanda_id: int) -> Optional[Comanda]:
        try:
            with get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(sql.SELECT_COMANDA, (comanda_id,))
                row = cursor.fetchone()
                if row:
                    return Comanda(id=row[0], numero=row[1], data_abertura=row[2], data_fechamento=row[3], valor_total=row[4])
                return None
        except sqlite3.Error as e:
            print(f"Erro ao obter comanda {comanda_id}: {e}")
            return None

    def obter_todos(self) -> List[Comanda]:
        try:
            with get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(sql.SELECT_TODAS_COMANDAS)
                rows = cursor.fetchall()
                return [Comanda(id=row[0], numero=row[1], data_abertura=row[2], data_fechamento=row[3], valor_total=row[4]) for row in rows]
        except sqlite3.Error as e:
            print(f"Erro ao obter todas as comandas: {e}")
            return []

    def atualizar(self, comanda: Comanda) -> bool:
        if comanda.id is None:
            print("Erro: Comanda sem ID não pode ser atualizada.")
            return False
        try:
            with get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(sql.UPDATE_COMANDA, (comanda.numero, comanda.data_abertura, comanda.data_fechamento, comanda.valor_total, comanda.id))
                return cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Erro ao atualizar comanda {comanda.id}: {e}")
            return False

    def excluir(self, comanda_id: int) -> bool:
        try:
            with get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(sql.DELETE_COMANDA, (comanda_id,))
                return cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Erro ao excluir comanda {comanda_id}: {e}")
            return False

from typing import List, Optional
import sqlite3
from contextlib import closing
from models.product import Product

class ProductRepo:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def _execute(self, query: str, params: tuple = ()):
        with closing(sqlite3.connect(self.db_path)) as conn:
            with closing(conn.cursor()) as cursor:
                cursor.execute(query, params)
                conn.commit()

    def create_product(self, product: Product) -> None:
        query = "INSERT INTO products (name, price, stock) VALUES (?, ?, ?)"
        self._execute(query, (product.name, product.price, product.stock))

    def get_product(self, product_id: int) -> Optional[Product]:
        query = "SELECT id, name, price, stock FROM products WHERE id = ?"
        with closing(sqlite3.connect(self.db_path)) as conn:
            with closing(conn.cursor()) as cursor:
                cursor.execute(query, (product_id,))
                row = cursor.fetchone()
                if row:
                    return Product(id=row[0], name=row[1], price=row[2], stock=row[3])
                return None

    def update_product(self, product: Product) -> None:
        query = "UPDATE products SET name = ?, price = ?, stock = ? WHERE id = ?"
        self._execute(query, (product.name, product.price, product.stock, product.id))

    def delete_product(self, product_id: int) -> None:
        query = "DELETE FROM products WHERE id = ?"
        self._execute(query, (product_id,))

    def list_products(self) -> List[Product]:
        query = "SELECT id, name, price, stock FROM products"
        with closing(sqlite3.connect(self.db_path)) as conn:
            with closing(conn.cursor()) as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()
                return [Product(id=row[0], name=row[1], price=row[2], stock=row[3]) for row in rows]
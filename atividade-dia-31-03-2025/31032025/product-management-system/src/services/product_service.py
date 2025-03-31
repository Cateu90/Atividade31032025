class ProductRepo:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def create_product(self, product):
        query = "INSERT INTO products (name, description, price) VALUES (?, ?, ?)"
        with self.db_connection:
            self.db_connection.execute(query, (product.name, product.description, product.price))

    def get_product(self, product_id):
        query = "SELECT * FROM products WHERE id = ?"
        cursor = self.db_connection.execute(query, (product_id,))
        row = cursor.fetchone()
        return row

    def update_product(self, product_id, product):
        query = "UPDATE products SET name = ?, description = ?, price = ? WHERE id = ?"
        with self.db_connection:
            self.db_connection.execute(query, (product.name, product.description, product.price, product_id))

    def delete_product(self, product_id):
        query = "DELETE FROM products WHERE id = ?"
        with self.db_connection:
            self.db_connection.execute(query, (product_id,))
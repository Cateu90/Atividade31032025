class DatabaseConnection:
    def __init__(self, db_file):
        self.db_file = db_file
        self.connection = None

    def open_connection(self):
        if self.connection is None:
            import sqlite3
            self.connection = sqlite3.connect(self.db_file)
            self.connection.row_factory = sqlite3.Row

    def close_connection(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None

    def execute_query(self, query, params=()):
        self.open_connection()
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        self.connection.commit()
        return cursor

    def fetch_all(self, query, params=()):
        cursor = self.execute_query(query, params)
        return cursor.fetchall()

    def fetch_one(self, query, params=()):
        cursor = self.execute_query(query, params)
        return cursor.fetchone()
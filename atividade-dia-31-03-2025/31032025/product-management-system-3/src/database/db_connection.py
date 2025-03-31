def get_db_connection():
    import sqlite3
    from contextlib import closing

    DATABASE_NAME = 'products.db'

    def connect():
        return sqlite3.connect(DATABASE_NAME)

    with closing(connect()) as connection:
        yield connection
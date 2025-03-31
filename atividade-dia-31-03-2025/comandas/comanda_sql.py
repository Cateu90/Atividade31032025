CREATE_TABLE = '''
CREATE TABLE IF NOT EXISTS comandas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    numero INTEGER NOT NULL,
    data_abertura DATETIME NOT NULL,
    data_fechamento DATETIME,
    valor_total REAL NOT NULL DEFAULT 0.0
)
'''

INSERT_COMANDA = '''
INSERT INTO comandas (numero, data_abertura)
VALUES (?, ?)
'''

SELECT_COMANDA = '''
SELECT id, numero, data_abertura, data_fechamento, valor_total
FROM comandas
WHERE id = ?
'''

SELECT_TODAS_COMANDAS = '''
SELECT id, numero, data_abertura, data_fechamento, valor_total
FROM comandas
'''

UPDATE_COMANDA = '''
UPDATE comandas
SET numero = ?, data_abertura = ?, data_fechamento = ?, valor_total = ?
WHERE id = ?
'''

DELETE_COMANDA = '''
DELETE FROM comandas
WHERE id = ?
'''

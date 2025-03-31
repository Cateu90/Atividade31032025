CREATE_TABLE = '''
CREATE TABLE IF NOT EXISTS caixas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data_abertura DATETIME NOT NULL,
    data_fechamento DATETIME,
    valor_inicial REAL NOT NULL,
    valor_final REAL
)
'''

INSERT_CAIXA = '''
INSERT INTO caixas (data_abertura, valor_inicial)
VALUES (?, ?)
'''

SELECT_CAIXA = '''
SELECT id, data_abertura, data_fechamento, valor_inicial, valor_final
FROM caixas
WHERE id = ?
'''

SELECT_TODOS_CAIXAS = '''
SELECT id, data_abertura, data_fechamento, valor_inicial, valor_final
FROM caixas
'''

UPDATE_CAIXA = '''
UPDATE caixas
SET data_abertura = ?, data_fechamento = ?, valor_inicial = ?, valor_final = ?
WHERE id = ?
'''

DELETE_CAIXA = '''
DELETE FROM caixas
WHERE id = ?
'''

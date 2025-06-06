import sqlite3
from datetime import datetime

# Conecta (ou cria) o banco de dados local
conn = sqlite3.connect('sensores.db')
cursor = conn.cursor()

# Cria as tabelas (se não existirem)
cursor.execute('''
CREATE TABLE IF NOT EXISTS sensor (
    id_sensor INTEGER PRIMARY KEY,
    tipo TEXT NOT NULL,
    unidade TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS localizacao (
    id_local INTEGER PRIMARY KEY,
    nome_estacao TEXT NOT NULL,
    cidade TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS leitura_sensor (
    id_leitura INTEGER PRIMARY KEY AUTOINCREMENT,
    id_sensor INTEGER,
    id_local INTEGER,
    valor REAL,
    data_hora TEXT,
    FOREIGN KEY (id_sensor) REFERENCES sensor(id_sensor),
    FOREIGN KEY (id_local) REFERENCES localizacao(id_local)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS alerta (
    id_alerta INTEGER PRIMARY KEY AUTOINCREMENT,
    id_leitura INTEGER,
    tipo_alerta TEXT,
    nivel TEXT,
    FOREIGN KEY (id_leitura) REFERENCES leitura_sensor(id_leitura)
)
''')

conn.commit()

# Funções CRUD

def inserir_sensor(id_sensor, tipo, unidade):
    cursor.execute('INSERT OR IGNORE INTO sensor VALUES (?, ?, ?)', (id_sensor, tipo, unidade))
    conn.commit()

def inserir_localizacao(id_local, nome_estacao, cidade):
    cursor.execute('INSERT OR IGNORE INTO localizacao VALUES (?, ?, ?)', (id_local, nome_estacao, cidade))
    conn.commit()

def inserir_leitura(id_sensor, id_local, valor, data_hora):
    cursor.execute('''
        INSERT INTO leitura_sensor (id_sensor, id_local, valor, data_hora) VALUES (?, ?, ?, ?)
    ''', (id_sensor, id_local, valor, data_hora))
    conn.commit()

def consultar_leituras():
    cursor.execute('SELECT * FROM leitura_sensor')
    return cursor.fetchall()

def atualizar_leitura(id_leitura, novo_valor):
    cursor.execute('UPDATE leitura_sensor SET valor = ? WHERE id_leitura = ?', (novo_valor, id_leitura))
    conn.commit()

def remover_leitura(id_leitura):
    cursor.execute('DELETE FROM leitura_sensor WHERE id_leitura = ?', (id_leitura,))
    conn.commit()

# Inserindo dados simulados (exemplo)

inserir_sensor(1, 'temperatura', '°C')
inserir_sensor(2, 'umidade', '%')
inserir_sensor(3, 'vibracao', 'binário')

inserir_localizacao(1, 'Estação Leste', 'São Paulo')
inserir_localizacao(2, 'Estação Norte', 'Campinas')

inserir_leitura(1, 1, 36.5, '2025-06-06 08:00:00')
inserir_leitura(2, 1, 82, '2025-06-06 08:00:00')
inserir_leitura(3, 1, 1, '2025-06-06 08:00:00')

# Testando consulta
leituras = consultar_leituras()
print("Leituras armazenadas:")
for leitura in leituras:
    print(leitura)

# Exemplo de atualização e remoção
atualizar_leitura(1, 37.0)
remover_leitura(2)

# Fechando conexão ao final
conn.close()

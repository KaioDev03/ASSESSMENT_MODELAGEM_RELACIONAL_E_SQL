import sqlite3

conn = sqlite3.connect('eventgo.db')
cursor = conn.cursor()

'''
    Cria as tabelas no banco de dados.
'''

'''
    Criação da tabela de usuarios
'''

cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
        nickname TEXT UNIQUE NOT NULL,
        senha TEXT NOT NULL,
        nome_completo TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        tipo_usuario TEXT CHECK(tipo_usuario IN ('organizador', 'participante')) NOT NULL
    )
''')

'''
    Criação da tabela de eventos
'''

cursor.execute('''
    CREATE TABLE IF NOT EXISTS eventos (
        id_evento INTEGER PRIMARY KEY AUTOINCREMENT,
        id_organizador INTEGER,
        titulo TEXT NOT NULL,
        descricao TEXT,
        data TEXT NOT NULL,
        hora TEXT NOT NULL,
        local TEXT NOT NULL,
        FOREIGN KEY (id_organizador) REFERENCES usuarios(id_usuario)
    )
''')

'''
    Criação da tabela de inscricoes
'''

cursor.execute('''
    CREATE TABLE IF NOT EXISTS inscricoes (
        id_inscricao INTEGER PRIMARY KEY AUTOINCREMENT,
        id_participante INTEGER,
        id_evento INTEGER,
        data_inscricao TEXT NOT NULL,
        UNIQUE (id_participante, id_evento),
        FOREIGN KEY (id_participante) REFERENCES usuarios(id_usuario),
        FOREIGN KEY (id_evento) REFERENCES eventos(id_evento)
    )
''')

'''
    Criação da tabela de feedback
'''

cursor.execute('''
    CREATE TABLE IF NOT EXISTS feedback (
        id_feedback INTEGER PRIMARY KEY AUTOINCREMENT,
        id_participante INTEGER,
        id_evento INTEGER,
        nota INTEGER CHECK(nota >= 1 AND nota <= 5),
        comentario TEXT,
        UNIQUE (id_participante, id_evento),
        FOREIGN KEY (id_participante) REFERENCES usuarios(id_usuario),
        FOREIGN KEY (id_evento) REFERENCES eventos(id_evento)
    )
''')

'''
    Inserindo dados na tabela
'''

usuarios = [
    ('organizador1', 'senha123', 'João Silva', 'joao@evento.com', 'organizador'),
    ('organizador2', 'senha456', 'Maria Souza', 'maria@evento.com', 'organizador'),
    ('participante1', 'senha789', 'Carlos Lima', 'carlos@evento.com', 'participante'),
    ('participante2', 'senha012', 'Ana Costa', 'ana@evento.com', 'participante')
]

cursor.executemany('''
    INSERT INTO usuarios (nickname, senha, nome_completo, email, tipo_usuario) 
    VALUES (?, ?, ?, ?, ?)
''', usuarios)

eventos = [
    (1, 'Conferência de Tecnologia', 'Uma conferência sobre as últimas tendências tecnológicas', '2024-12-15', '10:00:00', 'Auditório A'),
    (2, 'Workshop de Design', 'Um workshop prático sobre design gráfico', '2024-12-20', '14:00:00', 'Sala B')
]

cursor.executemany('''
    INSERT INTO eventos (id_organizador, titulo, descricao, data, hora, local) 
    VALUES (?, ?, ?, ?, ?, ?)
''', eventos)

inscricoes = [
    (3, 1, '2024-12-01'),
    (4, 1, '2024-12-02'),
    (3, 2, '2024-12-03')
]

cursor.executemany('''
    INSERT INTO inscricoes (id_participante, id_evento, data_inscricao) 
    VALUES (?, ?, ?)
''', inscricoes)

feedback = [
    (3, 1, 5, 'Ótimo evento, muito informativo!'),
    (4, 1, 4, 'Gostei, mas poderia ter mais tempo para perguntas.')
]

cursor.executemany('''
    INSERT INTO feedback (id_participante, id_evento, nota, comentario) 
    VALUES (?, ?, ?, ?)
''', feedback)

conn.commit()

conn.close()
print("Dados inseridos com sucesso!")
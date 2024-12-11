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
    ('participante2', 'senha012', 'Ana Costa', 'ana@evento.com', 'participante'),
    ('organizador3', 'senha321', 'Roberto Alves', 'roberto@evento.com', 'organizador'),
    ('participante3', 'senha654', 'Bruna Mendes', 'bruna@evento.com', 'participante'),
    ('participante4', 'senha987', 'Eduardo Pereira', 'eduardo@evento.com', 'participante'),
    ('organizador4', 'senha543', 'Fernanda Santos', 'fernanda@evento.com', 'organizador'),
    ('participante5', 'senha111', 'Juliana Duarte', 'juliana@evento.com', 'participante'),
    ('participante6', 'senha222', 'Leonardo Rocha', 'leonardo@evento.com', 'participante'),
    ('participante7', 'senha333', 'Paula Martins', 'paula@evento.com', 'participante'),
    ('organizador5', 'senha444', 'Pedro Gomes', 'pedro@evento.com', 'organizador'),
    ('participante8', 'senha555', 'Renata Silva', 'renata@evento.com', 'participante'),
    ('participante9', 'senha666', 'Lucas Carvalho', 'lucas@evento.com', 'participante')
]

cursor.executemany('''
    INSERT INTO usuarios (nickname, senha, nome_completo, email, tipo_usuario) 
    VALUES (?, ?, ?, ?, ?)
''', usuarios)

eventos = [
    (1, 'Conferência de Tecnologia', 'Uma conferência sobre as últimas tendências tecnológicas', '2024-12-15', '10:00:00', 'Auditório A'),
    (2, 'Workshop de Design', 'Um workshop prático sobre design gráfico', '2024-12-20', '14:00:00', 'Sala B'),
    (1, 'Hackathon 2024', 'Competição de programação para desenvolvimento de soluções inovadoras', '2024-12-10', '09:00:00', 'Laboratório C'),
    (3, 'Feira de Startups', 'Evento para networking e apresentação de startups', '2024-12-25', '11:00:00', 'Salão de Eventos D'),
    (4, 'Seminário de Sustentabilidade', 'Discussão sobre práticas sustentáveis no mercado', '2024-12-28', '15:00:00', 'Auditório E'),
    (2, 'Congresso de Marketing', 'Últimas estratégias e ferramentas para o marketing digital', '2024-12-22', '10:00:00', 'Sala F'),
    (5, 'Workshop de Fotografia', 'Aulas práticas sobre técnicas fotográficas', '2024-12-12', '08:30:00', 'Estúdio G'),
    (4, 'Palestra sobre Liderança', 'Técnicas para desenvolver habilidades de liderança', '2024-12-17', '13:00:00', 'Auditório H'),
    (3, 'Encontro de Desenvolvedores', 'Evento para troca de experiências entre desenvolvedores', '2024-12-19', '09:30:00', 'Sala I'),
    (1, 'Simulação de Negócios', 'Workshop sobre simulação de ambientes empresariais', '2024-12-26', '14:30:00', 'Sala J')
]

cursor.executemany('''
    INSERT INTO eventos (id_organizador, titulo, descricao, data, hora, local) 
    VALUES (?, ?, ?, ?, ?, ?)
''', eventos)

inscricoes = [
    (3, 1, '2024-12-01'),
    (4, 1, '2024-12-02'),
    (3, 2, '2024-12-03'),
    (5, 3, '2024-12-04'),
    (6, 4, '2024-12-05'),
    (7, 5, '2024-12-06'),
    (8, 6, '2024-12-07'),
    (9, 7, '2024-12-08'),
    (10, 8, '2024-12-09'),
    (11, 9, '2024-12-10'),
    (12, 10, '2024-12-11'),
    (13, 3, '2024-12-12'),
    (14, 4, '2024-12-13')
]

cursor.executemany('''
    INSERT INTO inscricoes (id_participante, id_evento, data_inscricao) 
    VALUES (?, ?, ?)
''', inscricoes)

feedback = [
    (3, 1, 5, 'Ótimo evento, muito informativo!'),
    (4, 1, 4, 'Gostei, mas poderia ter mais tempo para perguntas.'),
    (5, 3, 5, 'A competição foi incrível, me motivou muito!'),
    (6, 4, 3, 'O evento foi bom, mas poderia ser melhor organizado.'),
    (7, 5, 5, 'O workshop de fotografia foi excelente!'),
    (8, 6, 4, 'Gostei das palestras, mas faltou tempo para networking.'),
    (9, 7, 5, 'Evento muito produtivo! Ótimo para aprender novas estratégias.'),
    (10, 8, 3, 'A palestra foi boa, mas esperava algo mais interativo.'),
    (11, 9, 4, 'Bom evento, mas algumas sessões poderiam ser mais aprofundadas.'),
    (12, 10, 5, 'Workshop fantástico! Aprendi muito sobre simulação de negócios.'),
    (13, 3, 4, 'O Hackathon foi bem organizado e com boas ideias apresentadas.'),
    (14, 4, 5, 'O seminário foi muito relevante para o meu campo.')
]

cursor.executemany('''
    INSERT INTO feedback (id_participante, id_evento, nota, comentario) 
    VALUES (?, ?, ?, ?)
''', feedback)

conn.commit()

conn.close()
print("Dados inseridos com sucesso!")
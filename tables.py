import sqlite3

connection = sqlite3.connect('eventgo.db')

'''
    Cria as tabelas no banco de dados.
'''

cursor = connection.cursor()
cursor.execute('''
CREATE TABLE usuario (
    id_usuario INT PRIMARY KEY AUTO_INCREMENT,
    nickname VARCHAR(50) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL,
    nome_completo VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    tipo_usuario ENUM('organizador', 'participante') NOT NULL
);
''')
'''
    Criação da tabela de evento.
'''
cursor = connection.cursor()
cursor.execute('''
   CREATE TABLE eventos (
    id_evento INT PRIMARY KEY AUTO_INCREMENT,
    id_organizador INT,
    titulo VARCHAR(255) NOT NULL,
    descricao TEXT,
    data DATE NOT NULL,
    hora TIME NOT NULL,
    local VARCHAR(255) NOT NULL,
    FOREIGN KEY (id_organizador) REFERENCES usuario(id_usuario)
);
''')
'''
    Criação da tabela de inscrição
'''
cursor = connection.cursor()
cursor.execute('''
    CREATE TABLE inscricao (
    id_inscricao INT PRIMARY KEY AUTO_INCREMENT,
    id_participante INT,
    id_evento INT,
    data_inscricao DATE NOT NULL,
    UNIQUE (id_participante, id_evento),
    FOREIGN KEY (id_participante) REFERENCES usuario(id_usuario),
    FOREIGN KEY (id_evento) REFERENCES evento(id_evento)
);
''')
'''
    Criação da tabela de feedback
'''
cursor = connection.cursor()
cursor.execute('''
    CREATE TABLE feedback (
    id_feedback INT PRIMARY KEY AUTO_INCREMENT,
    id_participante INT,
    id_evento INT,
    nota INT CHECK(nota >= 1 AND nota <= 5),
    comentario TEXT,
    UNIQUE (id_participante, id_evento),
    FOREIGN KEY (id_participante) REFERENCES usuario(id_usuario),
    FOREIGN KEY (id_evento) REFERENCES evento(id_evento)
);
''')
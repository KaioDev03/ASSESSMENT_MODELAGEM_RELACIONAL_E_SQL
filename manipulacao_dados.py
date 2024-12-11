import sqlite3


conn = sqlite3.connect('eventgo.db')
cursor = conn.cursor()

cursor.execute('''
    UPDATE eventos
    SET titulo = 'Conferencia Tech'
    WHERE id_evento = 1;
''')

cursor.execute('''
    UPDATE usuarios
    SET nome_completo = 'Kaio França', senha = 'Senha0123'
    WHERE id_usuario = 2;
''')

cursor.execute('''
    DELETE FROM inscricoes
    WHERE id_inscricao IN (1, 2, 3);
''')

cursor.execute('''
    DELETE FROM avaliacoes
    WHERE nota < 2;
''')

cursor.execute('''
    DROP TABLE avaliacoes;
''')

conn.commit()

conn.close()

print("Atualizações e remoções concluídas com sucesso!")

print("Título do evento atualizado com sucesso.")
print("Nome e senha do usuário atualizados com sucesso.")
print("Inscrições removidas com sucesso.")
print("Feedbacks removidos com sucesso.")
print("Tabela de feedbacks removida com sucesso.")
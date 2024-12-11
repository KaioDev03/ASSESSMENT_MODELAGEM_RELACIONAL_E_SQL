import sqlite3

'''
    Renomeia a tabela feedback para avaliacoes
'''
conn = sqlite3.connect('eventgo.db')
cursor = conn.cursor()

cursor.execute('''
    ALTER TABLE avaliacoes RENAME TO feedback;
''')

conn.commit()

conn.close()

print("Tabela renomeada com sucesso!")
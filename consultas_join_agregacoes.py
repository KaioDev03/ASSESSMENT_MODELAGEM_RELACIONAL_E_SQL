import sqlite3

conn = sqlite3.connect('eventgo.db')
cursor = conn.cursor()

""" 
    Recuperar dados de usuários e seus eventos
    Faz um JOIN entre a tabela de usuários e eventos para listar quais eventos cada usuário organizou.
"""

consulta_usuarios_eventos = '''
SELECT u.nome_completo AS organizador, e.titulo AS evento, e.data, e.hora, e.local
FROM usuarios u
JOIN eventos e ON u.id_usuario = e.id_organizador;
'''
cursor.execute(consulta_usuarios_eventos)
usuarios_eventos = cursor.fetchall()
print("\nUsuários e seus eventos:")
for linha in usuarios_eventos:
    print(linha)

""" 
    Listar todos os eventos e seus organizadores
    Essa consulta lista os eventos com seus organizadores.
"""

consulta_eventos_organizadores = '''
SELECT e.titulo AS evento, u.nome_completo AS organizador
FROM eventos e
JOIN usuarios u ON e.id_organizador = u.id_usuario;
'''
cursor.execute(consulta_eventos_organizadores)
eventos_organizadores = cursor.fetchall()
print("\nEventos e seus organizadores:")
for linha in eventos_organizadores:
    print(linha)

""" 
    Mostrar todos os eventos, mesmo aqueles sem inscrições
    Aqui usamos um LEFT JOIN para garantir que eventos sem inscrições também apareçam.
"""

consulta_eventos_sem_inscricoes = '''
SELECT e.titulo AS evento, i.id_inscricao
FROM eventos e
LEFT JOIN inscricoes i ON e.id_evento = i.id_evento;
'''
cursor.execute(consulta_eventos_sem_inscricoes)
eventos_sem_inscricoes = cursor.fetchall()
print("\nTodos os eventos, mesmo sem inscrições:")
for linha in eventos_sem_inscricoes:
    print(linha)

""" 
    Contar o número de participantes em cada evento
    Essa consulta utiliza a função COUNT para contar quantos participantes estão inscritos em cada evento.
"""

contar_participantes_por_evento = '''
SELECT e.titulo AS evento, COUNT(i.id_participante) AS num_participantes
FROM eventos e
LEFT JOIN inscricoes i ON e.id_evento = i.id_evento
GROUP BY e.id_evento;
'''
cursor.execute(contar_participantes_por_evento)
participantes_eventos = cursor.fetchall()
print("\nNúmero de participantes em cada evento:")
for linha in participantes_eventos:
    print(linha)

""" 
    Calcular a nota média de feedbacks de um evento
    Calcula a média das notas de feedback para um evento específico.
"""

nota_media_feedbacks = '''
SELECT e.titulo AS evento, AVG(f.nota) AS media_nota
FROM eventos e
JOIN feedback f ON e.id_evento = f.id_evento
GROUP BY e.id_evento;
'''
cursor.execute(nota_media_feedbacks)
media_feedbacks = cursor.fetchall()
print("\nMédia de feedbacks por evento:")
for linha in media_feedbacks:
    print(linha)

""" 
    Agrupar resultados por evento ou organizador
    Essa consulta agrupa os eventos por organizador, mostrando quantos eventos cada um organizou.
"""

agrupar_eventos_organizador = '''
SELECT u.nome_completo AS organizador, COUNT(e.id_evento) AS num_eventos
FROM usuarios u
LEFT JOIN eventos e ON u.id_usuario = e.id_organizador
GROUP BY u.id_usuario;
'''
cursor.execute(agrupar_eventos_organizador)
eventos_por_organizador = cursor.fetchall()
print("\nNúmero de eventos por organizador:")
for linha in eventos_por_organizador:
    print(linha)

conn.close()

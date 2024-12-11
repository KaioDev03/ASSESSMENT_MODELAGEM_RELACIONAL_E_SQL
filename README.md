Olá Kaio,

Chegamos no momento mais importante! Você veio ao longo dos TPs se preparando e agora chegou a hora da sua avaliação. 

EventGo - Sistema de Inscrição em Eventos
Fala meus queridos! Galera, vocês acabam de ser contratados para desenvolver o banco de dados para o EventGo, uma plataforma simples que permite que organizadores criem eventos e participantes se inscrevam neles. O objetivo é facilitar a gestão de eventos como workshops, palestras, cursos e encontros. Eu fiz a mão para vocês e fui atrás dos requisitos e vocês terão de modelar de acordo com esses requisitos. Bora lá?

Requisitos e Regras de Negócio:

Usuários:
Cadastro: Cada usuário deve se registrar fornecendo um usuário (nickname) único e uma senha. Também devem informar nome completo e email.
Tipos de Usuário: Existem dois tipos de usuários:
Organizadores: Podem criar e gerenciar eventos.
Participantes: Podem se inscrever em eventos disponíveis.
Restrições:
O usuário (nickname) e o email devem ser únicos (UNIQUE).
Os campos usuário, senha, nome completo e email são obrigatórios (NOT NULL).
Eventos:
Criação: Organizadores podem criar eventos, fornecendo título, descrição, data, hora e local.
Gestão: Organizadores podem editar ou cancelar seus eventos.
Restrições:
Um evento é sempre criado por um único organizador.
Campos obrigatórios: título, data, hora, local (NOT NULL).
Inscrições:
Participação: Participantes podem se inscrever em múltiplos eventos.
Registro: Ao se inscrever, a data de inscrição é registrada.
Restrições:
Um participante não pode se inscrever mais de uma vez no mesmo evento.
Campos obrigatórios: data de inscrição (NOT NULL).
Feedback:
Avaliação: Após a realização do evento, participantes podem deixar um feedback.
Detalhes do Feedback: Inclui uma nota (1 a 5) e um comentário opcional.
Restrições:
O feedback deve estar associado a um participante e a um evento específico.
Um participante só pode deixar um feedback por evento.
Relacionamentos:
Usuários e Eventos:
One-to-Many: Um organizador pode criar vários eventos, mas um evento pertence a um único organizador.
Eventos e Inscrições:
Many-to-Many: Um evento pode ter vários participantes, e um participante pode se inscrever em vários eventos.
Esse relacionamento será modelado através de uma tabela intermediária Inscrições.
Eventos e Feedback:
One-to-Many: Um evento pode ter vários feedbacks, mas cada feedback está associado a um único evento e participante.
Buenas, agora vocês vão ter que me ajudar a modelar esse sistema para a gente ganhar uma grana vendendo ele. Lembrem que talvez nem todas as regras a gente consiga implementar no banco de dados.

Modelagem do Banco de Dados:
Identificar Entidades (Tabelas)
Definir Atributos
Estabelecer Relacionamentos
Aplicar Restrições
Normalização: Garantir que o modelo esteja normalizado até a Terceira Forma Normal (3FN).
A Saída dessa parte: Um documento modelado em alguma das ferramentas que vimos em sala de aula: brmodelo, draw.io, etc…
Criação de Tabelas e Objetos Utilizando SQL:
Escrever Scripts de Criação: Usar comandos CREATE TABLE para criar as tabelas com os campos e restrições definidos. Definir chaves primárias e estrangeiras usando PRIMARY KEY e FOREIGN KEY.
Implementar Restrições: Aplicar UNIQUE e NOT NULL nos campos apropriados.
Inserção de Dados: Inserir dados fictícios nas tabelas.
Modificação de Estruturas: Modificar o nome de uma tabela.
Saída dessa parte é os comandos SQL com as tabelas e atributos criados.
Manipulação de Dados:
Atualizações: Atualizar o título de um evento que está errado. Atualizar o nome e senha de um usuário.
Remoção by Id: Remover 3 inscrições erradas em um evento através da chave primária.
Remoção condicional: Remover feedbacks com base em uma condição específica criada por vocês. 
Remover uma tabela inteira: Remover toda a tabela de feedbacks.
A Saída dessa parte é o código SQL com o que foi requisitado.
Consultas com JOINs e Agregações:
Recuperar dados de usuários e seus eventos.
Listar todos os eventos e seus organizadores.
Mostrar todos os eventos, mesmo aqueles sem inscrições.
Usar COUNT para contar o número de participantes em cada evento.
Calcular a nota média de feedbacks de um evento.
Agrupar resultados por evento ou organizador.
Dica: Entender e aplicar corretamente as condições em joins para evitar resultados incorretos.
A Saída dessa parte é o código SQL com o que foi requisitado.
Instruções Finais:

Documentação: Documentar cada etapa do processo, incluindo diagramas ER e justificativas para decisões de modelagem.
Validação: Testar as restrições e chaves definidas inserindo dados que violem as regras de negócio para garantir que o banco de dados as impede corretamente.
Criatividade: Vocês podem adicionar funcionalidades extras, como status do evento (ativo, cancelado), categorias de eventos, ou confirmação de presença.
Dicas:

Análise Cuidadosa: Leia atentamente os requisitos e certifique-se de que todas as regras de negócio estão refletidas no modelo.
Simplificação: Mantenha o foco nas principais entidades e relacionamentos para evitar complexidade desnecessária.
Revisão de Conceitos: Revise conceitos de normalização e tipos de chaves para aplicá-los corretamente.
Testes Práticos: Após criar as tabelas, insira dados de teste e execute as consultas para verificar se os resultados são os esperados.
Uso de IAs: Sinal Vermelho 🔴 
Todas as partes deste trabalho devem ser da autoria do aluno. Qualquer uso de ferramentas generativas de IA, como ChatGPT, é proibido. O uso de IA generativa será considerado má conduta acadêmica e estará sujeito à aplicação do código disciplinar, pois as tarefas deste trabalho foram elaboradas para desafiar o aluno a desenvolver conhecimentos de base, pensamento crítico e habilidades de resolução de problemas. O uso da tecnologia de IA limitaria sua capacidade de desenvolver essas competências e de atingir os objetivos de aprendizagem desta disciplina.

O que entregar:

Documento Final: Deve ser bem estruturado, contendo todas as seções mencionadas acima. Certifique-se de que cada seção está claramente identificada e que o conteúdo é objetivo e completo. Será avaliada o capricho com o documento.
Inclua trechos de código SQL e, se possível, capturas de tela dos resultados.

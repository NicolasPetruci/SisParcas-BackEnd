INSERT INTO public.cargo (descricao) VALUES
    ('DONO'),
    ('ADM'),
    ('MESTRE'),
    ('DEFAULT');

INSERT INTO public.usuario (nome,email,telefone,senha,aniversario) VALUES
	 ('Nicolas Petruci Penga','nicolaspetrucipenga@gmail.com','(18) 99699-3141','$pbkdf2-sha256$30000$GoNwLgWAkNJaK4XwnlNqrQ$DIYMtONahCMwQhVFPdA8DPjjV80TjwOlE4zxhyl2MY4','2004-03-12'),
	 ('Lucas Roberto Gomes Molitor','lucasmolitor10@gmail.com','(18) 99806-8946','$pbkdf2-sha256$30000$Qsj5X8v5H4OwNqb0PkdIKQ$JO1aIrw7Uygo.qeCzmkhNlS5mO4LaZATwfE5M97gNoE','2004-02-26');

INSERT INTO public.usuario_cargo (id_usuario, id_cargo) VALUES
    (1,1),
    (1,2),
    (1,3),
    (1,4),
    (2,2),
    (2,4);
INSERT INTO public.genero (descricao) VALUES
    ('Fantasia'),
    ('Ficção Científica'),
    ('Terror'),
    ('Aventura'),
    ('RPG de Mesa'),
    ('Ação'),
    ('Mistério'),
    ('Drama'),
    ('Romance'),
    ('Supernatural'),
    ('Medieval'),
    ('Cyberpunk'),
    ('Horror'),
    ('Clássico'),
    ('Moderno'),
    ('Pós-apocalíptico'),
    ('Realidade Alternativa'),
    ('Histórico'),
    ('Fantástico'),
    ('Sobrenatural');

-- Inserindo dados para a tabela "tipo_evento"
INSERT INTO public.tipo_evento (descricao) VALUES
    ('Sessão de RPG'),
    ('Torneio'),
    ('Convenção'),
    ('Workshop'),
    ('Encontro'),
    ('Live'),
    ('Stream'),
    ('Lançamento'),
    ('Palestra'),
    ('Mesa Redonda'),
    ('Apresentação'),
    ('Festival'),
    ('Competição'),
    ('Evento Online'),
    ('Evento Presencial'),
    ('Reunião'),
    ('Feira'),
    ('Exposição'),
    ('Congresso'),
    ('Simpósio');

-- Inserindo dados para a tabela "usuario"
INSERT INTO public.usuario (nome, email, telefone, senha, aniversario) VALUES
    ('João da Silva', 'joao.silva@email.com', '11987654321', '$pbkdf2-sha256$30000$GoNwLgWAkNJaK4XwnlNqrQ$DIYMtONahCMwQhVFPdA8DPjjV80TjwOlE4zxhyl2MY4', '1990-05-10'),
    ('Maria Santos', 'maria.santos@email.com', '21987654321', '$pbkdf2-sha256$30000$GoNwLgWAkNJaK4XwnlNqrQ$DIYMtONahCMwQhVFPdA8DPjjV80TjwOlE4zxhyl2MY4', '1988-12-25'),
    ('Pedro Rodrigues', 'pedro.rodrigues@email.com', '12345678901', '$pbkdf2-sha256$30000$GoNwLgWAkNJaK4XwnlNqrQ$DIYMtONahCMwQhVFPdA8DPjjV80TjwOlE4zxhyl2MY4', '1995-08-15'),
    ('Ana Oliveira', 'ana.oliveira@email.com', '11999999999', '$pbkdf2-sha256$30000$GoNwLgWAkNJaK4XwnlNqrQ$DIYMtONahCMwQhVFPdA8DPjjV80TjwOlE4zxhyl2MY4', '1992-03-07'),
    ('Carlos Pereira', 'carlos.pereira@email.com', '21999999999', '$pbkdf2-sha256$30000$GoNwLgWAkNJaK4XwnlNqrQ$DIYMtONahCMwQhVFPdA8DPjjV80TjwOlE4zxhyl2MY4', '1985-01-15'),
    ('Luiza Almeida', 'luiza.almeida@email.com', '12345678910', '$pbkdf2-sha256$30000$GoNwLgWAkNJaK4XwnlNqrQ$DIYMtONahCMwQhVFPdA8DPjjV80TjwOlE4zxhyl2MY4', '1998-07-20'),
    ('Rafael Costa', 'rafael.costa@email.com', '11987654322', '$pbkdf2-sha256$30000$GoNwLgWAkNJaK4XwnlNqrQ$DIYMtONahCMwQhVFPdA8DPjjV80TjwOlE4zxhyl2MY4', '1991-09-28'),
    ('Beatriz Gomes', 'beatriz.gomes@email.com', '21987654322', '$pbkdf2-sha256$30000$GoNwLgWAkNJaK4XwnlNqrQ$DIYMtONahCMwQhVFPdA8DPjjV80TjwOlE4zxhyl2MY4', '1993-04-05'),
    ('Guilherme Santos', 'guilherme.santos@email.com', '12345678911', '$pbkdf2-sha256$30000$GoNwLgWAkNJaK4XwnlNqrQ$DIYMtONahCMwQhVFPdA8DPjjV80TjwOlE4zxhyl2MY4', '1989-06-12'),
    ('Letícia Silva', 'leticia.silva@email.com', '11999999998', '$pbkdf2-sha256$30000$GoNwLgWAkNJaK4XwnlNqrQ$DIYMtONahCMwQhVFPdA8DPjjV80TjwOlE4zxhyl2MY4', '1997-11-03'),
    ('Gustavo Oliveira', 'gustavo.oliveira@email.com', '21999999998', '$pbkdf2-sha256$30000$GoNwLgWAkNJaK4XwnlNqrQ$DIYMtONahCMwQhVFPdA8DPjjV80TjwOlE4zxhyl2MY4', '1994-02-18'),
    ('Fernanda Rodrigues', 'fernanda.rodrigues@email.com', '12345678912', '$pbkdf2-sha256$30000$GoNwLgWAkNJaK4XwnlNqrQ$DIYMtONahCMwQhVFPdA8DPjjV80TjwOlE4zxhyl2MY4', '1987-09-30'),
    ('Bruno Almeida', 'bruno.almeida@email.com', '11987654323', '$pbkdf2-sha256$30000$GoNwLgWAkNJaK4XwnlNqrQ$DIYMtONahCMwQhVFPdA8DPjjV80TjwOlE4zxhyl2MY4', '1996-05-22'),
    ('Alice Costa', 'alice.costa@email.com', '21987654323', '$pbkdf2-sha256$30000$GoNwLgWAkNJaK4XwnlNqrQ$DIYMtONahCMwQhVFPdA8DPjjV80TjwOlE4zxhyl2MY4', '1999-08-08'),
    ('Thiago Santos', 'thiago.santos@email.com', '12345678913', '$pbkdf2-sha256$30000$GoNwLgWAkNJaK4XwnlNqrQ$DIYMtONahCMwQhVFPdA8DPjjV80TjwOlE4zxhyl2MY4', '1986-03-17'),
    ('Camila Silva', 'camila.silva@email.com', '11999999997', '$pbkdf2-sha256$30000$GoNwLgWAkNJaK4XwnlNqrQ$DIYMtONahCMwQhVFPdA8DPjjV80TjwOlE4zxhyl2MY4', '1995-10-29'),
    ('Gabriel Oliveira', 'gabriel.oliveira@email.com', '21999999997', '$pbkdf2-sha256$30000$GoNwLgWAkNJaK4XwnlNqrQ$DIYMtONahCMwQhVFPdA8DPjjV80TjwOlE4zxhyl2MY4', '1990-01-04'),
    ('Isabela Rodrigues', 'isabela.rodrigues@email.com', '12345678914', '$pbkdf2-sha256$30000$GoNwLgWAkNJaK4XwnlNqrQ$DIYMtONahCMwQhVFPdA8DPjjV80TjwOlE4zxhyl2MY4', '1998-06-26'),
    ('Lucas Almeida', 'lucas.almeida@email.com', '11987654324', '$pbkdf2-sha256$30000$GoNwLgWAkNJaK4XwnlNqrQ$DIYMtONahCMwQhVFPdA8DPjjV80TjwOlE4zxhyl2MY4', '1992-12-11'),
    ('Sophia Costa', 'sophia.costa@email.com', '21987654324', '$pbkdf2-sha256$30000$GoNwLgWAkNJaK4XwnlNqrQ$DIYMtONahCMwQhVFPdA8DPjjV80TjwOlE4zxhyl2MY4', '1993-07-09');

-- Inserindo dados para a tabela "evento"
INSERT INTO public.evento (nome, descricao, "local", online, data_hora, id_tipo_evento) VALUES
    ('RPG Fest 2024', 'Festival de RPG com jogos, workshops e palestras', 'Centro de Convenções', false, '2024-06-15 10:00:00', 3),
    ('Torneio de D&D', 'Torneio de Dungeons & Dragons com premiação para os melhores jogadores', 'Loja de jogos', false, '2024-07-20 14:00:00', 2),
    ('Lançamento do RPG "A Lenda do Dragão"', 'Evento de lançamento do novo RPG de fantasia medieval', 'Livraria', false, '2024-08-10 19:00:00', 8),
    ('Workshop de RPG com GURPS', 'Workshop de RPG com o sistema GURPS, aprendendo as regras e criando personagens', 'Espaço Cultural', false, '2024-09-05 16:00:00', 4),
    ('Encontro de Mestres de RPG', 'Reunião de mestres de RPG para discutir técnicas e compartilhar experiências', 'Café', false, '2024-10-01 18:00:00', 5),
    ('Sessão de RPG online: "Acampamento Assombrado"', 'Sessão de RPG online com o sistema "Acampamento Assombrado"', 'Plataforma online', true, '2024-10-26 20:00:00', 1),
    ('Live de RPG: "O Enigma da Pirâmide"', 'Live de RPG com o sistema "O Enigma da Pirâmide", com interação do público', 'Plataforma de streaming', true, '2024-11-15 21:00:00', 6),
    ('Convenção de RPG de Ficção Científica', 'Convenção de RPG com foco em jogos de ficção científica', 'Centro de Convenções', false, '2024-12-07 10:00:00', 3),
    ('Workshop de RPG com Pathfinder', 'Workshop de RPG com o sistema Pathfinder, aprendendo as regras e criando personagens', 'Espaço Cultural', false, '2024-01-12 16:00:00', 4),
    ('Encontro de Jogadores de RPG', 'Reunião de jogadores de RPG para discutir jogos, sistemas e personagens', 'Bar', false, '2024-02-09 18:00:00', 5),
    ('Stream de RPG: "O Reino dos Elfos"', 'Stream de RPG com o sistema "O Reino dos Elfos", com narração detalhada e interação do público', 'Plataforma de streaming', true, '2024-03-18 20:00:00', 7),
    ('Lançamento do RPG "A Sombra do Dragão"', 'Evento de lançamento do novo RPG de fantasia épica', 'Livraria', false, '2024-04-20 19:00:00', 8),
    ('Torneio de RPG com FATE', 'Torneio de RPG com o sistema FATE, com premiação para os melhores jogadores', 'Loja de jogos', false, '2024-05-11 14:00:00', 2),
    ('RPG Fest 2025', 'Festival de RPG com jogos, workshops e palestras', 'Centro de Convenções', false, '2025-06-21 10:00:00', 3),
    ('Workshop de RPG com Apocalypse World', 'Workshop de RPG com o sistema Apocalypse World, aprendendo as regras e criando personagens', 'Espaço Cultural', false, '2025-07-13 16:00:00', 4),
    ('Encontro de Mestres de RPG', 'Reunião de mestres de RPG para discutir técnicas e compartilhar experiências', 'Café', false, '2025-08-17 18:00:00', 5),
    ('Sessão de RPG online: "A Cidade Perdida"', 'Sessão de RPG online com o sistema "A Cidade Perdida"', 'Plataforma online', true, '2025-09-28 20:00:00', 1),
    ('Live de RPG: "O Tesouro Escondido"', 'Live de RPG com o sistema "O Tesouro Escondido", com interação do público', 'Plataforma de streaming', true, '2025-10-19 21:00:00', 6),
    ('Convenção de RPG de Horror', 'Convenção de RPG com foco em jogos de terror', 'Centro de Convenções', false, '2025-11-16 10:00:00', 3),
    ('Workshop de RPG com Call of Cthulhu', 'Workshop de RPG com o sistema Call of Cthulhu, aprendendo as regras e criando personagens', 'Espaço Cultural', false, '2025-12-08 16:00:00', 4);

-- Inserindo dados para a tabela "mestre"
INSERT INTO public.mestre (ativo, id_usuario) VALUES
    (true, 1),
    (true, 3),
    (false, 5),
    (true, 7),
    (true, 9),
    (true, 11),
    (false, 13),
    (true, 15),
    (true, 17),
    (false, 19),
    (true, 2),
    (false, 4),
    (true, 6),
    (true, 8),
    (false, 10),
    (true, 12),
    (true, 14),
    (false, 16),
    (true, 18),
    (true, 20);

-- Inserindo dados para a tabela "rpg"
INSERT INTO public.rpg (nome, descricao, id_mestre) VALUES
    ('O Senhor dos Anéis: RPG', 'RPG baseado no universo de O Senhor dos Anéis, com foco em aventura e combate', 1),
    ('Dungeons & Dragons 5e', 'RPG de fantasia medieval clássico, com foco em exploração e combate', 3),
    ('Call of Cthulhu', 'RPG de horror cósmico, com foco em investigação e terror psicológico', 5),
    ('Vampire: The Masquerade', 'RPG de vampiros, com foco em intriga e sobrevivência', 7),
    ('FATE', 'RPG de sistema narrativo, com foco em flexibilidade e criatividade', 9),
    ('Star Wars: RPG', 'RPG baseado no universo de Star Wars, com foco em aventura espacial e combate', 11),
    ('Cyberpunk 2020', 'RPG cyberpunk com foco em ação e intriga em um mundo futurista', 13),
    ('Shadowrun', 'RPG cyberpunk com elementos de fantasia, com foco em ação e intriga', 15),
    ('Numenera', 'RPG de ficção científica com elementos de fantasia, com foco em exploração e descobertas', 17),
    ('The Witcher RPG', 'RPG baseado no universo de The Witcher, com foco em aventura e combate', 19),
    ('World of Darkness', 'RPG de horror e suspense com foco em sobrevivência e conspirações', 2),
    ('Mutants & Masterminds', 'RPG de super-heróis, com foco em ação e criação de personagens', 4),
    ('Savage Worlds', 'RPG de sistema genérico, com foco em aventura e combate rápido', 6),
    ('GURPS', 'RPG de sistema genérico, com foco em realismo e detalhamento', 8),
    ('Pathfinder', 'RPG de fantasia medieval com foco em exploração e combate', 10),
    ('Apocalypse World', 'RPG de sistema narrativo, com foco em storytelling e resolução de conflitos', 12),
    ('Dungeon World', 'RPG de fantasia medieval com foco em exploração e combate', 14),
    ('Blades in the Dark', 'RPG de espionagem e crime com foco em intriga e ação', 16),
    ('Monsterhearts', 'RPG de romance e horror com foco em relacionamentos e drama', 18),
    ('Masks: A New Generation', 'RPG de super-heróis com foco em drama e crescimento pessoal', 20);

-- Inserindo dados para a tabela "sessao"
INSERT INTO public.sessao (nome, descricao, data_hora, temporada, numero, id_rpg) VALUES
    ('A Caverna Perdida', 'O grupo explora uma caverna em busca de um artefato mágico', '2024-03-10 19:00:00', 1, 1, 1),
    ('O Ataque dos Orcs', 'O grupo enfrenta um ataque de orcs e precisa defender a vila', '2024-03-17 19:00:00', 1, 2, 2),
    ('O Mistério do Antigo Templo', 'O grupo investiga um antigo templo e enfrenta os horrores que lá residem', '2024-03-24 19:00:00', 1, 1, 3),
    ('A Noite da Caçada', 'Os vampiros caçam em uma cidade, e o grupo precisa sobreviver', '2024-03-31 19:00:00', 1, 1, 4),
    ('A Missão Secreta', 'O grupo é contratado para realizar uma missão perigosa, com muitas reviravoltas', '2024-04-07 19:00:00', 1, 1, 5),
    ('A Batalha de Endor', 'O grupo participa da Batalha de Endor, lutando contra o Império Galáctico', '2024-04-14 19:00:00', 1, 1, 6),
    ('O Hacker da Cidade', 'O grupo precisa hackear um sistema de segurança para impedir um crime', '2024-04-21 19:00:00', 1, 1, 7),
    ('O Ataque dos Meta-humanos', 'O grupo precisa impedir um ataque de meta-humanos à cidade', '2024-04-28 19:00:00', 1, 1, 8),
    ('A Caçada ao Tesouro Perdido', 'O grupo busca um tesouro perdido em um mundo pós-apocalíptico', '2024-05-05 19:00:00', 1, 1, 9),
    ('O Monstro da Floresta', 'O grupo precisa derrotar um monstro que aterroriza a floresta', '2024-05-12 19:00:00', 1, 1, 10),
    ('A Conspiração Secreta', 'O grupo descobre uma conspiração que ameaça o mundo', '2024-05-19 19:00:00', 1, 1, 11),
    ('A Guerra dos Super-heróis', 'O grupo participa de uma guerra entre super-heróis', '2024-05-26 19:00:00', 1, 1, 12),
    ('A Caçada ao Bandido', 'O grupo precisa capturar um bandido perigoso', '2024-06-02 19:00:00', 1, 1, 13),
    ('O Enigma da Masmorra', 'O grupo explora uma masmorra em busca de um artefato', '2024-06-09 19:00:00', 1, 1, 14),
    ('A Batalha Final', 'O grupo enfrenta o grande vilão da história', '2024-06-16 19:00:00', 1, 1, 15),
    ('A Rebelião dos Mutantes', 'O grupo se junta a uma rebelião de mutantes contra o governo', '2024-06-23 19:00:00', 1, 1, 16),
    ('A Missão Impossível', 'O grupo é desafiado a realizar uma missão quase impossível', '2024-06-30 19:00:00', 1, 1, 17),
    ('O Terror na Cidade', 'O grupo precisa lidar com uma série de eventos sobrenaturais na cidade', '2024-07-07 19:00:00', 1, 1, 18),
    ('A Guerra dos Reinos', 'O grupo é envolvido em uma guerra entre reinos', '2024-07-14 19:00:00', 1, 1, 19),
    ('O Nascimento de um Herói', 'O grupo acompanha a jornada de um herói em formação', '2024-07-21 19:00:00', 1, 1, 20);

    -- Inserindo dados para a tabela "usuario_cargo"
INSERT INTO public.usuario_cargo (id_cargo, id_usuario) VALUES
    (1, 1), -- João da Silva - DONO
    (2, 3), -- Pedro Rodrigues - ADM
    (3, 7), -- Rafael Costa - MESTRE
    (4, 9), -- Guilherme Santos - DEFAULT
    (1, 10), -- Letícia Silva - DONO
    (2, 12), -- Fernanda Rodrigues - ADM
    (3, 14), -- Bruno Almeida - MESTRE
    (4, 16), -- Thiago Santos - DEFAULT
    (1, 17), -- Gabriel Oliveira - DONO
    (2, 19), -- Lucas Almeida - ADM
    (3, 2), -- Maria Santos - MESTRE
    (4, 4), -- Ana Oliveira - DEFAULT
    (1, 5), -- Carlos Pereira - DONO
    (2, 6), -- Luiza Almeida - ADM
    (3, 8), -- Beatriz Gomes - MESTRE
    (4, 11), -- Gustavo Oliveira - DEFAULT
    (1, 13), -- Isabela Rodrigues - DONO
    (2, 15), -- Camila Silva - ADM
    (3, 18), -- Alice Costa - MESTRE
    (4, 20); -- Sophia Costa - DEFAULT

-- Inserindo dados para a tabela "genero_rpg"
INSERT INTO public.genero_rpg (id_rpg, id_genero) VALUES
    (1, 1), -- O Senhor dos Anéis: RPG - Fantasia
    (2, 1), -- Dungeons & Dragons 5e - Fantasia
    (3, 13), -- Call of Cthulhu - Horror
    (4, 1), -- Vampire: The Masquerade - Fantasia
    (5, 1), -- FATE - Fantasia
    (6, 2), -- Star Wars: RPG - Ficção Científica
    (7, 2), -- Cyberpunk 2020 - Ficção Científica
    (8, 2), -- Shadowrun - Ficção Científica
    (9, 2), -- Numenera - Ficção Científica
    (10, 1), -- The Witcher RPG - Fantasia
    (11, 13), -- World of Darkness - Horror
    (12, 2), -- Mutants & Masterminds - Ficção Científica
    (13, 1), -- Savage Worlds - Fantasia
    (14, 1), -- GURPS - Fantasia
    (15, 1), -- Pathfinder - Fantasia
    (16, 1), -- Apocalypse World - Fantasia
    (17, 1), -- Dungeon World - Fantasia
    (18, 2), -- Blades in the Dark - Ficção Científica
    (19, 13), -- Monsterhearts - Horror
    (20, 2); -- Masks: A New Generation - Ficção Científica

-- Inserindo dados para a tabela "jogador_rpg"
INSERT INTO public.jogador_rpg (id_rpg, id_usuario) VALUES
    (1, 2), -- Dungeons & Dragons 5e - Maria Santos
    (2, 4), -- Call of Cthulhu - Ana Oliveira
    (3, 6), -- Vampire: The Masquerade - Luiza Almeida
    (4, 8), -- FATE - Beatriz Gomes
    (5, 10), -- Star Wars: RPG - Letícia Silva
    (6, 12), -- Cyberpunk 2020 - Fernanda Rodrigues
    (7, 14), -- Shadowrun - Bruno Almeida
    (8, 16), -- Numenera - Thiago Santos
    (9, 18), -- The Witcher RPG - Alice Costa
    (10, 20), -- World of Darkness - Sophia Costa
    (11, 1), -- Mutants & Masterminds - João da Silva
    (12, 3), -- Savage Worlds - Pedro Rodrigues
    (13, 5), -- GURPS - Carlos Pereira
    (14, 7), -- Pathfinder - Rafael Costa
    (15, 9), -- Apocalypse World - Guilherme Santos
    (16, 11), -- Dungeon World - Gustavo Oliveira
    (17, 13), -- Blades in the Dark - Isabela Rodrigues
    (18, 15), -- Monsterhearts - Camila Silva
    (19, 17), -- Masks: A New Generation - Gabriel Oliveira
    (20, 19); -- The Witcher RPG - Lucas Almeida

-- Inserindo dados para a tabela "jogador_sessao"
INSERT INTO public.jogador_sessao (id_sessao, id_usuario) VALUES
    (1, 2), -- A Caverna Perdida - Maria Santos
    (2, 4), -- O Ataque dos Orcs - Ana Oliveira
    (3, 6), -- O Mistério do Antigo Templo - Luiza Almeida
    (4, 8), -- A Noite da Caçada - Beatriz Gomes
    (5, 10), -- A Missão Secreta - Letícia Silva
    (6, 12), -- A Batalha de Endor - Fernanda Rodrigues
    (7, 14), -- O Hacker da Cidade - Bruno Almeida
    (8, 16), -- O Ataque dos Meta-humanos - Thiago Santos
    (9, 18), -- A Caçada ao Tesouro Perdido - Alice Costa
    (10, 20), -- O Monstro da Floresta - Sophia Costa
    (11, 1), -- A Conspiração Secreta - João da Silva
    (12, 3), -- A Guerra dos Super-heróis - Pedro Rodrigues
    (13, 5), -- A Caçada ao Bandido - Carlos Pereira
    (14, 7), -- O Enigma da Masmorra - Rafael Costa
    (15, 9), -- A Batalha Final - Guilherme Santos
    (16, 11), -- A Rebelião dos Mutantes - Gustavo Oliveira
    (17, 13), -- A Missão Impossível - Isabela Rodrigues
    (18, 15), -- O Terror na Cidade - Camila Silva
    (19, 17), -- A Guerra dos Reinos - Gabriel Oliveira
    (20, 19); -- O Nascimento de um Herói - Lucas Almeida
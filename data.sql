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
    (2,4)
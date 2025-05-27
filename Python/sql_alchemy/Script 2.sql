use cinema;

create table if not exists atores (
	id int not null auto_increment,
	nome varchar(50) not null,
	titulo_filme varchar(50) not null,
	primary key(id),
	foreign key (titulo_filme) references filmes(titulo)
	);

insert into filmes(titulo, genero, ano) values('Forest Gump', 'Drama', 1994);

select * from atores;




create database cinema;
use cinema;

create table filmes (
	titulo varchar(50) not null,
	genero varchar(50) not null,
	ano int not null,
	primary key(titulo)
	);

insert into filmes(titulo, genero, ano) values('Forest Gump', 'Drama', 1994);

select * from filmes;

exemplos abaixo:

SELECT TOP 1 local_tcp_port 
FROM sys.dm_exec_connections
WHERE local_tcp_port IS NOT NULL;

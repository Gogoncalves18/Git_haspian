use SYNECO_2023;

select * from SSPImport order by ID desc;

select * from testeSYNECO order by ID desc;

USE SYNECO_2023; SELECT * FROM testeSYNECO ORDER BY ID DESC;

sp_help testeSYNECO;
sp_help SSPImport;

drop table testeSYNECO;

INSERT INTO testeSYNECO VALUES (3500, '10', 'Serra', '2022-11-04 10:55:20.247', 1, 1);



create table testeSYNECO (
	ID int not null Identity(1,1),
	OP nvarchar(60),
	OPER nvarchar(60),
	SEQOPER nvarchar(60),
	DESCOPER nvarchar(100),
	CODPECA nvarchar(60),
	DESCPECA nvarchar(100),
	PRODAUX1 nvarchar(200),
	PRODAUX2 nvarchar(200),
	PRODAUX3 nvarchar(200),
	PRODAUX4 nvarchar(200),
	MAQ nvarchar(60),
    CENTROCUSTO nvarchar(60),
    PLANDTINI nvarchar(40),
    PLANHRINI nvarchar(16),
	PLANDTFIM nvarchar(40),
	PLANHRFIM nvarchar(16),
	PLANQTY int,
	CYCLEQTY INT,
	PLANTMUNIT real,
	PLANTMSETUP REAL,
	ACAO INT,
	STATUS INT,
	DateRegist datetime,
	dateProcess datetime
	);

create table testeSYNECO (
	ID int not null Identity(1,1),
	OP int null,
	OPER nvarchar(60),
	
	DESCOPER nvarchar(100),
	DateRegist datetime not null,
	ACAO int not null,
	STATU int not null,
	);


	drop table testeSYNECO;

	create table testeSYNECO (
	ID int not null Identity(1,1),
	OP int null,
	OPER int null,
	DESCOPER nvarchar(100) null,
	DateRegist datetime null,
	ACAO int not null
	);

select * from testeSYNECO order by ID asc;

UPDATE testeSYNECO SET DESCOPER='olha' WHERE op='1000';

DELETE from testeSYNECO WHERE OP='1005';

INSERT INTO testeSYNECO VALUES (null, '10');

sp_help testeSYNECO;


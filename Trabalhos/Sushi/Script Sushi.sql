create table entregas (
	idsushi int not null Identity(1,1),
	numentrega int,
	uidcliente varchar(100),
	datapedido date,
	horapedido time,
	horapedidopronto time,
	horapedidoaceito time,
	horapedidoentregue time,
	tempopedido time,
	txentrega numeric(4, 2),
	txmotoboy numeric(4, 2),
	motoboy varchar(30),
    nomecliente varchar(50),
    telefone varchar(20),
    rua varchar(100),
	numresd varchar(10),
	cidade varchar(30),
	lat varchar(50) not null,
	long varchar(50) not null,
	latcoleta varchar(50) not null,
	longcoleta varchar(50) not null,
	obspedido varchar(150),
	iddelivery varchar(10),
	dist varchar(5),
	tempodist varchar(5)
	);

	insert into dbo.entregas(numentrega, uidcliente, datapedido, horapedido, horapedidopronto,
	horapedidoaceito, horapedidoentregue, tempopedido, txentrega, txmotoboy, motoboy,
	nomecliente, telefone, rua, numresd, cidade, lat, long, latcoleta, longcoleta,
	obspedido)  values (
	1,
	'usssooooxxx',
	'2024-08-02',
	'20:20:49',
	'18:50:12',
	'18:50:55',
	'19:00:23',
	'00:10:00',
	'3.0',
	'7.0',
	'Bruno',
	'Aline santos',
	'4199991234',
	'adenauer',
	231,
	'CWB',
	'-25.4354243',
	'-49.22411629999999',
	'-25.42294',
	'-49.1233',
	'Jotamane'
	);



	use foodyd;
	drop table dbo.entregas;

	select * from dbo.entregas order by idsushi desc;

	create table entregas (
	idsushi int not null Identity(1,1),
	numentrega int,	
	datapedido date,
	horapedido time,
	txentrega numeric(4, 2),
	lat varchar(50) not null);

	insert into dbo.entregas (numentrega, datapedido, horapedido, txentrega) values (
	1,
	'2024-08-01',
	'18:20:49',
	'13.450');

	insert into dbo.entregas (numentrega, datapedido, horapedido, txentrega, lat) values (
	1,
	'2024-08-01',
	'18:20:49',
	'3.0',
	'-49.22411629999999');

	select datapedido from dbo.entregas
		where idsushi = (select max(idsushi) from dbo.entregas);
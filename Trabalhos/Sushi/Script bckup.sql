use master;restore database ncrcolibri from disk = 'C:\Program Files\Microsoft SQL Server\MSSQL15.ECSQLEXPRESS\MSSQL\Backup\nc.bak' with replace;

use ncrcolibri;

select * from dbo.historico_operacao_geral order by dt_hora desc;

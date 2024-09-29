# Entity Framework do CSharp

- framework ORM é um sistema de migração de dados entre objetos relacionais

## Para iniciar um projeto
- na pasta raiz digitar "dotnet new console" , para criar a pasta dos arquivos
- os pacotes podem ser inseridos dentro da "Solution" através do "packages"
- após adicionar os pacotes, é necessário executar "dotnet restore" para atualizar os pacotes
- Executar o Migrations para olhar o BD pós tipagem 

## Pacotes necessários

- dotnet add package Microsoft.EntityFrameworkCore.SqlServer 
    - Pacote para conectar com o SQL
- dotnet add package Microsoft.EntityFrameworkCore.Design   
- dotnet add package Microsoft.EntityFrameworkCore.Tools.DotNet
    - Para trabalhar com algumas ferramentas do migrations     


## Migrations

- Necessario instalar a ferramenta no terminal com config global: **dotnet tool install --global dotnet-ef**. Ela ficara com chamada dotnet-ef
- " dotnet-ef migrations add inicial " para iniciar uma migration dentro do Space do codigo, coloca 3 códigos na pasta Migrations
- " dotnet-ef database update " atualiza o ambiente recém instalado e executa no BD o modelamento

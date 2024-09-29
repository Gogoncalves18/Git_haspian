namespace ConsoleApp.CS1;

using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using global::CS1;
using Microsoft.EntityFrameworkCore;


// Sempre que trabalhamos com o EF do .net precisamos de uma class que 
// possui as classes de conexao com o BD. Neste caso a minha classe que 
// sempre tem um nome com a palavra Context junto para normatizar, "LivroContext"
// ela herda do EF a class "DbContext" que dara os principais metodos
public class LivroContext : DbContext
{
    // Dentro desta class podemos utilizar um propriedade de "DbContext" chamada "DbSet", 
    // que possui tipagens para trabalhar com o BD, neste caso usamos ela para tipar a table
    // Livro que criamos na class Livro.cs, dando a ela acessos get e set. Se tivesse mais tabelas
    // eu teria que colocar todas aqui
    public DbSet<Livro> Livros { get; set; }

    // Metodo especifico do EF para conectar ao BD, ele deve ser protegido e sobre escrito
    // sobre o seguinte metodo "OnConfiguring" ao qual passamos uma tipagem e metodos do 
    // "DbContextOptionsBuilder" sob a variavel "optionsBuilder"
    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
    {
        // Como esta variavel "optionsBuilder" esta instanciada em uma class "DbContextOptionsBuilder"
        // podemo chamar um novo metodo ".UseSqlServer" para passagem da str de conexao, composta por:
        /*
        @ - para iniciar
        Server= com o nome do meu servidor, neste caso "(localdb)\mssqllocaldb"
        Database= nome da instancia do BD "EFDemo"
        Trusted_Connection=True  , para os casos que meu BD nao possui login proprio, apenas 
        autenticacao do Windows

        Posteriormente podemos executar os cmd no terminal para criar o BD
        */
        optionsBuilder
            .UseSqlServer(@"Server=(localdb)\mssqllocaldb;Database=EFDemo; Trusted_Connection=True;", options => options.MaxBatchSize(2));

        // O " options => options.MaxBatchSize(2) " e uma opcao do UseSqlServer para executar um numero
        // de operacoes por lote, neste caso sera duas operacoes, isto e, se tenho 10 registro, ele 
        // executara 5 queries no sql
    }

    // Este metodo server para modelagem do BD
    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        // Se eu nao apontar que quero que a tabela se chama livro ao inves de livros (ele sempre cria no plural),
        // eu posso passar para o EF que minha class livro chamara no BD Livro atraves do ".ToTable("Livro")"
        modelBuilder.Entity<Livro>()
            .ToTable("Livro");

        // o ".HasKey()"  e o cmd que defino qual e a PK da table, porem ela precisa percorrer
        // todas linhas de minha tabela, portanto uso uma lambda dentro, onde o "p" representa
        // a linha da minha coluna "LivroID" que foi definida na class "livro.cs", assim ""p.LivroId"
        // indica que cada linha desta coluna sera uma ".HasKey"
        modelBuilder.Entity<Livro>()
            .HasKey(p => p.LivroId);

        // Ja os dados adicionais sao definidos como ".Property" e tambem recebem o mesmo esquema
        // de lambda. Porem quando apos ele eu derivo mais um ".HasColumnType", estou definindo 
        // uma caracterisca adicional, neste caso o tipo do dado que a tabela deve aceitar
        modelBuilder.Entity<Livro>()
            .Property(p => p.Titulo)
            .HasColumnType("varchar(50)");
    }
}


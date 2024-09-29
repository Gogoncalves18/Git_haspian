using System;
using CS1;
using Microsoft.EntityFrameworkCore;

namespace ConsoleApp.CS1;

class Program
{
    // Classe comum sem retorno "void"
    static void Main(string[] args)

    {
        // Instancio sobre o meu context para poder enviar os comandos
        using (var db = new CS1.LivroContext())
        {
            // O ".Database" e uma class do EF e dentro dela eu tenho os principais comandos.
            // ".EnsureCreated()" cria o BD, mas e importante executar o Migrations manualmente 
            // para ver o como ficou a estrutura do BD, olhar o arquivo "Aula_EFCore.md"

            // >>>> db.Database.EnsureCreated();

            // ".Livros" e o DbSet de minha conexao com o BD e nela executamos o cmd ".Add(new )" para
            // adicionar novo obj que sera as instancias da tabela, nele apontaremos o Livro que vem da
            // class "Livro.cs" e passamos como um Dict as informacoes da table

            db.Livros.Add(new Livro { Titulo = "Dominio da mente", Autor = "Tchachu", AnoPublicacao = 2001 });
            db.Livros.Add(new Livro { Titulo = "Tu nnão é o cara", Autor = "Mestre Sr", AnoPublicacao = 2010 });
            db.Livros.Add(new Livro { Titulo = "Foco é tudo", Autor = "Cuca Beludo", AnoPublicacao = 2005 });
            db.Livros.Add(new Livro { Titulo = "Prefiro Python", Autor = "GOG", AnoPublicacao = 2024 });
            db.Livros.Add(new Livro { Titulo = "Dominio das mulheres", Autor = "Tchachu", AnoPublicacao = 1982 });

            // Para consolidar os dados no BD
            db.SaveChanges();

            Console.WriteLine("\n >>>>>>> DaDos Gravados <<<<<<\n");
            Console.WriteLine("\n >>>>>>> Lista dos dados que foram gravados: <<<<<<\n");

            db.Livros.ForEachAsync(d => Console.WriteLine($"Título : {d.Titulo} - Autor : {d.Autor}")).ToString();

        }
    }
}
using System;
using CS2;
using Microsoft.EntityFrameworkCore;

namespace ConsoleApp.CS2;

// Aula 4 - https://www.youtube.com/watch?v=oG5B_KvVByA&list=PLgBAHVu7jSqD1hoCVZ65XGX1DWCftB643&index=4

class Program
{
    // Classe comum sem retorno "void"
    static void Main(string[] args)

    {
        // Instancio sobre o meu context para poder enviar os comandos
        using (var db = new LivroContext())
        {
            // Deleta o BD
            db.Database.EnsureDeleted();

            // Cria do zero o BD
            db.Database.EnsureCreated();

            // Se sobre ainda alguma tabela, eu detono ela, o ".Any()" me diz se ha algo em Livros
            if (db.Livros.Any())
            {

            }

            db.Livros.Add(new Livro { Titulo = "Dominio da mente", Autor = "Tchachu", AnoPublicacao = 2001 });
            db.Livros.Add(new Livro { Titulo = "Tu não é o cara", Autor = "Mestre Sr", AnoPublicacao = 2010 });
            db.Livros.Add(new Livro { Titulo = "Foco é tudo", Autor = "Cuca Beludo", AnoPublicacao = 2005 });
            db.Livros.Add(new Livro { Titulo = "Prefiro Python", Autor = "GOG", AnoPublicacao = 2024 });
            db.Livros.Add(new Livro { Titulo = "Dominio das mulheres", Autor = "Tchachu", AnoPublicacao = 1982 });

            // Para consolidar os dados no BD

            db.SaveChanges();

            Console.WriteLine("\n >>>>>>> Consulta Comum <<<<<<\n");

            var cons = new ConsultasSql();

            cons.ConsultaComum("Dominio");

            Console.WriteLine("\n >>>>>>> Consulta Com Linq <<<<<<\n");

            cons.ConsultaComLinq("Dominio");

            Console.WriteLine("\n >>>>>>> Consulta Com Interpolation <<<<<<\n");

            cons.ConsultaComInterPolation("Dominio");


            Console.WriteLine("\n >>>>>>> Consulta Com Interpolation QUERY INJECTION, sem problemas <<<<<<\n");

            cons.ConsultaComInterPolationSqlInjection("2010");

            Console.WriteLine("\n >>>>>>> Consulta Com Interpolation QUERY INJECTION com CODIGO PARA DERRUBAR o SQL  <<<<<<\n");

            cons.ConsultaComInterPolationSqlInjection("2010; DROP TABLE Livro;");

            Console.WriteLine("\n !!!!! ACABEI DE DELETAR A TABELA COM O SQL QUERIE INJECTION  !!!!!!\n");


        }
    }
}
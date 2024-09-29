using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using ConsoleApp.CS2;
using CS2;
using Microsoft.EntityFrameworkCore;

namespace ConsoleApp.CS2
{
    public class ConsultasSql
    {
        public void ConsultaComum(string filtro)
        {
            // Necessario instanciar o contexto para poder fazer a consulta
            using (var db = new LivroContext())
            {
                // Forma de executar um query com parametro passado, e importate escrever as queries desta forma para 
                // não termos Inject Query em um parametro passado. Neste caso o proprio framework se encarrega de validar o 
                // parametro. O ".FromSqlRaw" e o metodo utilizado quando usamos a escrita igual ao SQL e ele forma
                // uma lista de objetos (respostas da pesquisa)
                var livros = db.Livros.FromSqlRaw("SELECT * FROM dbo.Livro WHERE Titulo LIKE '%' + @p0 + '%'", filtro).ToList();

                Console.WriteLine("\n Resultado : \n");
                livros.ForEach(x => Console.WriteLine($"Titulo => {x.Titulo} / Ano => {x.AnoPublicacao}"));
            }
        }

        public void ConsultaComLinq(string filtro)
        {
            using (var db = new LivroContext())
            {
                /*
                O ".FromSqlRaw" sempre retornara um Iquerieable, que por sua vez posso executar um novo select dentro do 
                resultado do primeiro select, pegando o titulo que tenha no nome "Domínio" e o ano do livro igual 1982.
                Depois convertemos para lista o resultado.
                */
                var livros = db.Livros.FromSqlRaw("SELECT * FROM dbo.Livro WHERE Titulo LIKE '%' + @p0 + '%'", filtro)
                                                .Where(x => x.AnoPublicacao == 1982)
                                                .ToList();

                Console.WriteLine("\n Resultado : \n");
                livros.ForEach(x => Console.WriteLine($"Titulo => {x.Titulo} / Ano => {x.AnoPublicacao}"));
            }
        }


        public void ConsultaComInterPolation(string filtro)
        {
            using (var db = new LivroContext())
            {
                /*
                Possibilidade de concatenar uma ou mais str dentro da propria query.
                */

                var livros = db.Livros.FromSqlInterpolated($"SELECT * FROM dbo.Livro WHERE Titulo LIKE '%' + {filtro} + '%'")
                                                .ToList();

                Console.WriteLine("\n Resultado : \n");
                livros.ForEach(x => Console.WriteLine($"Titulo => {x.Titulo} / Ano => {x.AnoPublicacao}"));
            }
        }

        public void ConsultaComInterPolationSqlInjection(string filtro)
        {
            using (var db = new LivroContext())
            {
                /*
                Formato incorreto de escrever a querie, neste caso o "Program.cs" gera um sql injection que 
                derruba a tabela que existia.
                */

                var sql = $"SELECT * FROM dbo.Livro WHERE AnoPublicacao = {filtro}";

                var livros = db.Livros.FromSqlRaw(sql)
                                                .ToList();

                Console.WriteLine("\n Resultado : \n");
                livros.ForEach(x => Console.WriteLine($"Titulo => {x.Titulo} / Ano => {x.AnoPublicacao}"));
            }
        }

    }
}
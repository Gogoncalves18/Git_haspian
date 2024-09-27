using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;

namespace ConsoleApp.Aula5;

class Program
{
    private static ApplicationContext? dbContext;

    static async Task Main(string[] args)
    {
        Console.WriteLine("\nAula Prática 05 - BD no .NET:\n");
        Console.WriteLine("---------------------------------------------------------------------\n");

        dbContext = new ApplicationContext();

        Console.WriteLine("\n>>>>>>>>> VERIFICANDO O BD <<<<<<<<<<<\n");

        // Teste de conexão
        var canConnect = await dbContext.Database.CanConnectAsync();

        if (!canConnect)
        {
            Console.WriteLine(" >>>>>> NÃO CONECTOU NO BD <<<<<<<");
            return;
        }
        Console.WriteLine("\n >>>>>> CONEXÃO ESTABELECIDA COM O BD <<<<<<<\n");

        // Verifica se o BD existe, caso contrario ele cria
        await dbContext.Database.EnsureCreatedAsync();

        Console.WriteLine("\n >>>>>> BD criado <<<<<<<\n");

        await Querys();
    }

    public static async Task Querys()
    {
        var query = await dbContext.Alunos.AsNoTracking()
                                    .Include(x => x.Cursos)
                                    .ThenInclude(x => x.Curso)
                                    .Select(x => new
                                    {
                                        AlunoId = x.Id,
                                        AlunoNome = x.Nome,
                                        CursoCompleto = x.Cursos.Select(c => new
                                        {
                                            c.CursoID,
                                            c.DataInscricao,
                                            c.PeriodoAtual,
                                            c.Curso.TempoMesesPeriodo,
                                            c.Curso.Periodos,
                                            Periodoteorico = Math.Ceiling(((DateTime.Now - c.DataInscricao).TotalDays / 30) / 6)
                                        })
                                    }).ToListAsync();


        // Filtro
        var alunosQuery = query.Where(x => x.CursoCompleto.Any(c => c.PeriodoAtual < c.Periodoteorico)).ToList();

        // filtro 2

        var cursosInstituicaoPresencial = await dbContext.Instituicoes
                                                            .Include(i => i.Cursos)
                                                            .Where(i => i.Tipo == 2)
                                                            .SelectMany(c => c.Cursos)
                                                            .Select(c => c.Id)
                                                            .ToListAsync();

        // Filtro 3
        var alunosAtrasadosPresencial = alunosQuery.Where(a => a.CursoCompleto.Select(c => c.CursoID)
                                                                .Any(x => cursosInstituicaoPresencial.any(c => c == x)))
                                                                .ToList();
    }

    public static async Task GeraAlunos()
    {
        var cursos = await dbContext.Cursos.ToListAsync();
        var rand = new Random();

        for (int i = 0; i < 10; i++)
        {
            var aluno = new Aluno
            {
                Id = Guid.NewGuid(),
                Nome = $"Aluno {i}",
                DataNascimento = new DateTime(rand.Next(1985, 2005), rand.Next(1, 13), rand.Next(1, 28)),
                Email = $"aluno{i}@escola.com.br",
                Cursos = new List<CursoAluno>()
            };

            var qtdCurso = rand.Next(1, 5);

            for (int k = 0; k < qtdCurso; k++)
            {
                var cursoIndex = rand.Next(0, 4);

                var curso = cursos[cursoIndex];
                var vinculoCursoAluno = new CursoAluno()
                {
                    CursoID = curso.Id,
                    Curso = curso,
                    Aluno = aluno,
                    AlunoId = aluno.Id,
                    DataInscricao = new DateTime(rand.Next(2018, 2021), 1, 1),
                    PeriodoAtual = rand.Next(1, curso.Periodos)
                };

                if (!aluno.Cursos.Any(c => c.CursoID == vinculoCursoAluno.CursoID))
                {
                    aluno.Cursos.Add(vinculoCursoAluno);
                }
            }

            await dbContext.AddAsync(aluno);
        }

        // Salva todos os alunos no BD
        await dbContext.SaveChangesAsync();
    }

    public static async Task CarregaCursosAsync()
    {
        var instituicoes = await dbContext.Instituicoes.ToListAsync();

        var curso1 = new Curso()
        {
            Nome = "Ciencia da Comp",
            Periodos = 8,
            TempoMesesPeriodo = 6,
            Valor = 5000,
            Instituicao = instituicoes[0]
        };

        var curso2 = new Curso()
        {
            Nome = "Eng da Comp",
            Periodos = 10,
            TempoMesesPeriodo = 8,
            Valor = 7000,
            Instituicao = instituicoes[0]
        };

        var curso3 = new Curso()
        {
            Nome = "Analise Sistemas",
            Periodos = 4,
            TempoMesesPeriodo = 3,
            Valor = 3000,
            Instituicao = instituicoes[0]
        };

        var curso4 = new Curso()
        {
            Nome = "Dev Device",
            Periodos = 4,
            TempoMesesPeriodo = 5,
            Valor = 4000,
            Instituicao = instituicoes[0]
        };

        var curso5 = new Curso()
        {
            Nome = "DBA",
            Periodos = 5,
            TempoMesesPeriodo = 4,
            Valor = 6000,
            Instituicao = instituicoes[1]
        };

        await dbContext.AddAsync(curso1);
        await dbContext.AddAsync(curso2);
        await dbContext.AddAsync(curso3);
        await dbContext.AddAsync(curso4);
        await dbContext.AddAsync(curso5);

        await dbContext.SaveChangesAsync();

    }

    public static async Task CargaInstituicaoAsync()
    {
        Console.WriteLine("\nInforme o nome da instituição: ");
        var nome = Console.ReadLine();

        Console.WriteLine("\nInforme o tipo da instituição (EAD, EADPresencial, Presencial): ");
        var tipo = Console.ReadLine();

        var instituicao1 = new Instituicao()
        {
            Nome = nome,
            Tipo = Enum.Parse<Instituicao.TipoInstituicao>(tipo)
        };

        Console.WriteLine("\nInforme OUTRA instituição: ");
        nome = Console.ReadLine();

        Console.WriteLine("\nInforme OUTRO tipo de instituição (EAD, EADPresencial, Presencial): ");
        tipo = Console.ReadLine();

        var instituicao2 = new Instituicao()
        {
            Nome = nome,
            Tipo = Enum.Parse<Instituicao.TipoInstituicao>(tipo)
        };


        dbContext.Add(instituicao1);
        await dbContext.AddAsync(instituicao2);

        // Executa no BD
        await dbContext.SaveChangesAsync();
    }
}
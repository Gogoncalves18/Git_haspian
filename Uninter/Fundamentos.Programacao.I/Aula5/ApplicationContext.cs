using System.Reflection;
using Microsoft.EntityFrameworkCore.SqlServer;
using System.Collections.Generic;
using System;
using Microsoft.EntityFrameworkCore;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace ConsoleApp.Aula5;

public class ApplicationContext : DbContext
{
    private const string stringDeConexao = "Data Source=YOGA9I\\SQLEXPRESS; Initial Catalog=AULA5;Integrated Security=True; Connect Timeout=15;Encrypt=False;TrustServerCertificate=False";

    public DbSet<Aluno> Alunos { get; set; }
    public DbSet<Curso> Cursos { get; set; }
    public DbSet<Instituicao> Instituicoes { get; set; }

    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
    {
        var serverVersion = new SqlServerVersion(new Version(15, 0, 2120));

        optionsBuilder.UseSqlServer(stringDeConexao, serverVersion).EnableDetailedErrors();
    }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.ApplyConfigurationsFromAssembly(Assembly.GetExecutingAssembly());
    }
}

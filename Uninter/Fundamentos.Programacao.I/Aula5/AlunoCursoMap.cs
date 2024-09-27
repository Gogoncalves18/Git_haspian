using ConsoleApp.Aula5;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;

namespace ConsoleApp.Aula5;

public class AlunoCursoMap : IEntityTypeConfiguration<CursoAluno>
{
    public void Configure(EntityTypeBuilder<CursoAluno> builder)
    {
        // Chave Composta entre dois tipos de entidade do BD
        builder.HasKey(x => new { x.AlunoId, x.CursoID });
        builder.HasOne(x => x.Aluno).WithMany(x => x.Cursos).HasForeignKey(x => x.AlunoId);
        builder.HasOne(x => x.Curso).WithMany(x => x.Alunos).HasForeignKey(x => x.CursoID);


        builder.Property(x => x.DataInscricao);
        builder.Property(x => x.PeriodoAtual);

    }
}


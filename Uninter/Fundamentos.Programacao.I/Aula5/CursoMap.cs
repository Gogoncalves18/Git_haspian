using ConsoleApp.Aula5;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;

namespace ConsoleApp.Aula5;

public class CursoMap : IEntityTypeConfiguration<Curso>
{
    public void Configure(EntityTypeBuilder<Curso> builder)
    {
        builder.ToTable("Curso");
        builder.HasKey(x => x.Id);
        builder.Property(x => x.Id).ValueGeneratedOnAdd();
        builder.Property(x => x.Nome).HasMaxLength(100);
        builder.Property(x => x.Valor).HasPrecision(2);
        builder.Property(x => x.Periodos);
        builder.Property(x => x.TempoMesesPeriodo);
    }
}

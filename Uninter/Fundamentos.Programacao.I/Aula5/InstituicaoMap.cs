using System.Runtime.CompilerServices;
using System.Security.Cryptography.X509Certificates;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;


namespace ConsoleApp.Aula5;



public class InstituicaoMap : IEntityTypeConfiguration<Instituicao>
{
    public void Configure(EntityTypeBuilder<Instituicao> builder)
    {
        builder.ToTable("Instituicao");
        builder.HasKey(x => x.Id);
        builder.Property(x => x.Id).ValueGeneratedOnAdd();
        builder.Property(x => x.Nome).HasMaxLength(100);
        builder.Property(x => x.Tipo).HasConversion(toDb => toDb.GetHashCode(), fromDb => (Instituicao.TipoInstituicao)fromDb);

        // Uma instituicao tem muitos cursos e cada curso aponta para uma instuicao
        builder.HasMany(x => x.Cursos).WithOne(x => x.Instituicao);
    }
}


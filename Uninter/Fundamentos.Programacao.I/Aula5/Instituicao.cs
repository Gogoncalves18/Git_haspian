using System.Collections.Generic;

namespace ConsoleApp.Aula5;

public class Instituicao
{

    public enum TipoInstituicao
    {
        EAD,
        EADPresencial,
        Presencial
    }
    public int Id { get; set; }
    public string? Nome { get; set; }
    public TipoInstituicao Tipo { get; set; }
    public required List<Curso> Cursos { get; set; }
}

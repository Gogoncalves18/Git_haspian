using System;

namespace ConsoleApp.Aula5;
// Modelagem de N:N do BD
public class CursoAluno
{
    public Curso Curso { get; set; }
    public int CursoID { get; set; }
    public Aluno Aluno { get; set; }
    public Guid AlunoId { get; set; }

    public DateTime DataInscricao { get; set; }
    public int PeriodoAtual { get; set; }

}

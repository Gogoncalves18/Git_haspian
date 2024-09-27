using System;
using System.Collections.Generic;

namespace ConsoleApp.Aula5;

public class Aluno
{
    public Guid Id { get; set; }
    public string Nome { get; set; }
    public string Email { get; set; }
    public DateTime DataNascimento { get; set; }

    public List<CursoAluno> Cursos { get; set; }
}

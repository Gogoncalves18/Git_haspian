using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace CS2;

// Classe que representa um table do SQL, cada classe como esta deve representar
// uma table 
public class Livro
{
    // Cada propriedade abaixo sera a abstracao das colunas da tabela onde
    // cada uma delas precisa de um get e set para obter ou setar valores
    public int LivroId { get; set; }
    public required string Titulo { get; set; }
    public required string Autor { get; set; }
    public int AnoPublicacao { get; set; }
}
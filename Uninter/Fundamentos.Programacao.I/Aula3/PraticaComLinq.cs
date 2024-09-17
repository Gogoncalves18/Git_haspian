using System.Xml;
// Tudo o trecho da linha 10 para baixo foi executado no LINQPAD

namespace Aula3;

public class PraticaComLinq
{
    public void Ex_linq_1()
    {
        // Listas para percorrer
        string[] nomes = { "Joao", "Silva", "Antonio", "Maria", "Joana", "Matheus", "Alan", "Julian" };
        string[] materias = { "Programacao I", "Algoritimos II", "Redes", "Calculo II", "SO" };

        // Funcao para sorteio
        Random rand = new Random();

        // Lista para receber as avaliacoes, aqui estou inicalizando uma lista de "Avaliacao"
        // que e uma CLASS que escrevi nas linhas abaio para tornar publico as propriedades
        List<Avaliacao> avaliacoes = new List<Avaliacao>();

        // Para cada estudante, eu percorro as materias para gravar 3 infos, nome + materia + nota
        // ao qual terei todas as materias para todos os estudantes.
        foreach (var nomeEstudante in nomes)
        {
            foreach (var materia in materias)
            {
                // Aqui estou estanciando a avaliação, gerando uma instancia para cada estudante
                var avaliacao = new Avaliacao()
                {
                    // Gero as propriedades de cada instancia
                    Nome = materia,
                    NomeAluno = nomeEstudante,
                    // Faço dois random, um para o inteiro e outro para o decimal
                    //  e executo um PARSE(concateno) e logo depois transformo em decimal
                    Nota = decimal.Parse($"{rand.Next(0, 10)}, {rand.Next(0, 10)}")
                };

                // Adiciono a lista a instancia completa
                avaliacoes.Add(avaliacao);
            }
        }

        // Query 1 - LINQ Query
        // From aqui e o mesmo que for, para cada nome em nomes
        var queryEstudantes = from n in nomes
                                  // let funciona como uma variavel que guardara o select do proximo from.
                                  // dentro do () executo um select ou for da seguinte forma:
                                  // Para cada avaliacao em avaliacoes, seleciona apenas os registros (eles estao como obj)
                                  // devido ao construtor da linha 27, que estao com nome igual ao nome que esta vindo de n,
                                  // da linha "from n in nomes" e selecionando o "a" q sao as avaliacoes.
                                  // Apos converte uma uma nova lista com .ToList()
                                  // Isto tudo foi instaciado em "avaliacoesEstudantes"
                              let avaliacoesEstudantes = (from a in avaliacoes
                                                          where a.NomeAluno == n
                                                          select a).ToList()

                              // Executa um novo select atraves de um construtor que ira gerar instancias de 8 estudantes
                              // cada uma delas tera um nome, uma media e uma lista com todas as infos de "avaliacoesEstudantes"
                              select new estudante()
                              {
                                  Avaliacoes = avaliacoesEstudantes,
                                  Nome = n,
                                  Media = avaliacoesEstudantes.Average(x => x.Nota)
                              };

        // Query 2 - LINQ Fluent Sintax

        // Pego a query que fiz acima para inteirar na query debaixo
        var estudantesList = queryEstudantes.ToList();

        // Instancia em "estudanteMaiorNota" todo o resultado construido abaixo, atraves de:
        // Aproveito a lista da query anterior em "estudantesList"
        // Executa um select de varios resultado trazendo uma lista com os seguintes criterios
        // em sua respectiva ordem:
        // "a" representa avaliacao dentro de avaliacoes
        // "m" somente de uma determinada materia
        // "n" ordenada por nota 
        // "nam" trazendo o nome do aluno, se tirar esta linha, ele monta a instancia toda do estudante
        // .FirstOrDefault() pega apenas um estudante de maior nota ao inves de uma lista
        // de estudantes em ordem descrescente de nota.
        var estudanteMaiorNota = estudantesList.SelectMany(a => a.Avaliacoes)
                                                .Where(m => m.Nome == "Programacao I")
                                                .OrderByDescending(n => n.Nota)
                                                .Select(nam => nam.NomeAluno)
                                                .FirstOrDefault();

        // Media de notas por materia:
        // A diferenca aqui e que agrupo as materias de todos os aluno por "m"
        // Depois a dica e gerar um seexta com um construtor anomimo gerando instancias com "x => new"
        // dentro dele abro propriedade onde:
        // "X" se refere a cada item do grupo de "GroupBy",
        // a .key seria o nome de cada instancia do grupo
        // Na "MediaNota" fazemos uma media da materia em meio a varios alunos, este e feito
        // por uma lambda onde "med" representa as notas de todos alunos por materia em "x"
        var queryMediaNotasPorMat = estudantesList.SelectMany(a => a.Avaliacoes)
                                                    .GroupBy(m => m.Nome)
                                                    .Select(x => new
                                                    {
                                                        materia = x.Key,
                                                        MediaNota = x.Average(med => med.Nota)
                                                    });


        // Query 2 - LINQ Fluent Sintax - Alunos do Calculo II com a letra A

        // Nesta query usamos um operador de criterio multiplo &&
        // Convertemos o nome do aluno para minusculas com a funcao  .ToLower()
        // Por fim usamos .Contains("a") para encontrar nome com a letra "a"
        var queryAlunosCalComLetraA = estudantesList.SelectMany(a => a.Avaliacoes)
                                                    .Where(m => m.Nome == "Calculo II" && m.NomeAluno.ToLower().Contains("a"))
                                                    .OrderByDescending(n => n.Nota);

    }

    // class

    public class estudante
    {
        // Propriedade que estou tornando public para escrever e ler
        public string Nome { get; set; }
        public decimal Media { get; set; }
        public List<Avaliacao> Avaliacoes { get; set; }
    }

    public class Avaliacao
    {
        public string Nome { get; set; }
        public string NomeAluno { get; set; }
        public decimal Nota { get; set; }
    }
}

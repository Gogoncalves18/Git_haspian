using System.Runtime.Serialization;

namespace Aula2;

public class PraticaManipulacaoCollections
{
    public void Exercicio4()
    {
        var arrayBase = new int[50];
        for (int i = 0; i < arrayBase.Length; i++)
        {
            arrayBase[i] = i * 10;
        }

        // Abaixo fazemos um CASTING explicito para 3 tipos de colecao
        //ao

        IEnumerable<int> enumeravel = arrayBase;
        IList<int> lista = arrayBase;
        ICollection<int> colecao = arrayBase;

        int countE = 0;
        int countL = 0;
        int countC = 0;

        // ENUMERAVEIS, este metodo nao possui enumeracoes dos elementos, portanto
        // a contagem dele precisa ser diferente
        foreach (var item in enumeravel)
        {
            Console.WriteLine($"\n Itens do ENUMERAVEL => POS {countE} Item {item} - Com Total de {countE + 1} Elementos.");
            countE++;
            if (countE == 30)
            {
                Console.WriteLine($"\n Trigéssimo Elemento => POS {countE} Item {item} - Com Total de {countE + 1} Elementos.");

            }
        }

        // LISTAS, este metodo possui um enumeravel dentro dele
        foreach (var item in lista)
        {
            Console.WriteLine($"\n Itens da LISTA => POS {countL} Item {item} - Com Total de {lista.Count} Elementos.");
            countL++;

        }

        // Lista e a unica que me permite acessar um elemento por posicao
        Console.WriteLine($"\n Trigéssimo Elemento da Lista => Item {lista[30]}.");


        // COLLECTIONS, este metodo possui um enumeravel dentro dele
        foreach (var item in colecao)
        {
            Console.WriteLine($"\n Itens da COLLECTION => POS {countC} Item {item} - Com Total de {colecao.Count} Elementos.");
            countC++;

            if (countC == 30)
            {
                Console.WriteLine($"\n Trigéssimo Elemento => POS {countC} Item {item} - Com Total de {countC + 1} Elementos.");

            }
        }
    }
}

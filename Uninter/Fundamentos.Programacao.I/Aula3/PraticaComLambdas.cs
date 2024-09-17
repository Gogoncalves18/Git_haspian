using System.Reflection.Metadata.Ecma335;

namespace Aula3;

public class PraticaComLambdas
{
    public void Ex1()
    {
        // ACTION soo lambdas VOID isto e, elas nao retornam nada
        Action<DateTime> lambda1 = (DateTime data) =>
        {
            Console.WriteLine(data.ToString("dd/MM/yyyy HH:mm:ss"));
        };

        // Usando a lambda como um metodo qq

        lambda1(new DateTime(2010, 01, 30));
        lambda1(new DateTime(1999, 12, 31, 10, 05, 30));

        // Lambda para incrementar um num recebido pela funcao

        var lambda2 = (int vlr) => { return vlr + 1; };

        Console.WriteLine($"Lambda 2, passo vlr 4 e incremento com 1 => {lambda2(4)}");

        // Lambda criado usando:
        // Converto para string
        // Obtenho o nome do objeto
        // Converto para um vlr e somo eles, de um obj para um valor

        var lambda3 = (object vlr1, object vlr2) => { return vlr1.ToString() + vlr2.ToString() + 1; };
        var lambda4 = (object vlr1, object vlr2) => { return vlr1.GetType().ToString() + vlr2.GetType().ToString() + 1; };
        var lambda5 = (object vlr1, object vlr2) => { return vlr1.GetHashCode() + vlr2.GetHashCode() + 1; };

        Console.WriteLine($"Lambda 3, passo vlr 4 e 2, incremento com 1 => {lambda3(4, 2)}");
        Console.WriteLine($"Lambda 4, passo vlr 4 e 2, incremento com 1 => {lambda4(4, 2)}");
        Console.WriteLine($"Lambda 5, passo vlr 4 e 2, incremento com 1 => {lambda5(4, 2)}");

        // Nesta a FUNC converte os 3 dados em OBJ ao contrario da LAMBDA 3 e 8, veja que aqui apenas agrupo 
        Func<object, object, object> lambda6 = (object vlr1, object vlr2) => { return $"{vlr1} + {vlr2} + 1"; };

        // Aqui eu pego uma funcao FUNC<..., ..., ...> que entra dois objetos e sai um INT, ele 
        // uso o .GetHashCode() para pegar o vlr do obj, este caso seria o mesmo que o LAMBDA5
        Func<object, object, int> lambda7 = (object vlr1, object vlr2) => { return vlr1.GetHashCode() + vlr2.GetHashCode() + 1; };

        Func<object, object, string> lambda8 = (object vlr1, object vlr2) => { return $"{vlr1} + {vlr2}" + 1; };

        Console.WriteLine($"Lambda 6, passo vlr 4 e 2, incremento com 1 => {lambda6(4, 2)}");
        Console.WriteLine($"Lambda 7, passo vlr 4 e 2, incremento com 1 => {lambda7(4, 2)}");
        Console.WriteLine($"Lambda 8, passo vlr 4 e 2, incremento com 1 => {lambda8(4, 2)}");
    }

    public void Ex2()
    {
        // Inicializa um array com 10 vlrs

        var arrayBase = new int[10];
        for (int i = 0; i < arrayBase.Length; i++)
        {
            arrayBase[i] = i;
        }
        IEnumerable<int> enumerable = arrayBase;
        int counter = 0;


        Console.WriteLine($"Array bruto - {arrayBase}");

        foreach (var item in arrayBase)
        {
            Console.WriteLine($"POS {counter} = vlr {item}");
            counter++;
        }

        Console.WriteLine($"Array vlrs desencapsulados - {arrayBase}");
        Console.WriteLine("LINHA 64");

        var arrayBase1 = new int[5] { 1, 1, 1, 1, 1 };

        // Lambda que multilica dois array
        /*
        - Nesta linha abaixo abro um FUNC (funcao) que recebe dois enumerable com type INT e vou retornar um enumarable INT,
            esta primeira parte pega somente os tipos de entrada e saida.
        - multiVetores sera minha funcao que recebe dois array de valores.
        - Apos abro a primeira Lambda, ao qual informo o que vou receber(IEnumerable), o tipo dele <int> e um nome para o dado
            recebido, finalizando a primeira parte com => e abro { }; para jogar o codigo ali dentro.
        */
        Func<IEnumerable<int>, IEnumerable<int>, IEnumerable<int>> multiVetores = (IEnumerable<int> vetor1, IEnumerable<int> vetor2) =>
        {
            /*
            -   Nesta linha informo que receberei um LIST de type <int>.
            -   Intancio nele um LIST e dentro do () precisamos colocar o numero de posicoes.
                que neste caso sera o tamanho do primeiro array que receberei
            */
            List<int> result = new List<int>(vetor1.Count());
            // Intero sobre o array
            foreach (var item in vetor1)
            {
                /*
                -   Para cada valor do primeiro array, item do vetor1, pegamos:
                -   Cada item do vetor2, "operacao resolve primeiro o que esta dentro do lambda",
                    que e representado por x, e para cada x do vetor2 eu multiplico pelo valor do item
                    do vetor1.
                -   Apos percorrer todo o vetor2, ele somada todos os resultados e grava no array RESULT
                -   Sendo assim terei um novo array com o numero de elementes do vetor1
                */
                result.Add(vetor2.Sum(x => x * item));
            }
            Console.WriteLine(result);
            // Retorno o RESULT para funcao que esta invocando
            return result;
        };

        // Invoco a fx multiVetores(vetor1, vetor2)
        var result = multiVetores(arrayBase, arrayBase1);
        counter = 0;

        foreach (var item in result)
        {
            // Imprimo os resultados comparando as posicoes do primeiro vetor com o RESULT final
            Console.WriteLine($"POS {counter} = vlr {item}");
            counter++;
        }


    }
    // CONVERTER PARA UM EXTENSION METHOD 6.35 SEG

    /*
    public static class ExtensionMethodLambda
    {
        public static IEnumerable<T> MultiplicaPorEnumerable<T>(this IEnumerable<T> origem, IEnumerable<T> vetor2, Func<IEnumerable<T>, IEnumerable<T>, IEnumerable<T>> funcaoMultiplicar)
        {
            return funcaoMultiplicar(origem, vetor2);
        }
    }
    */

}

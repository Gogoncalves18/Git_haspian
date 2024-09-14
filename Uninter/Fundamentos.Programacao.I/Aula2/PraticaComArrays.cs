using System.Security.Cryptography.X509Certificates;
using Microsoft.VisualBasic;

namespace ConsoleApp.Aula2
{

    public class PraticaComArrays
    {
        public void Exercicio1()
        {
            // Declaro que trabalharei com int e depois declaro que sera um array
            // atraves de [], instancio ela em um array de 100mil posicoes de num
            // inteiros
            int[] arrayIntLinear = new int[100000];

            // O for eu populo ela linearmente, isto e, as 100mil posicoes 
            // atraves de:
            /* Defino o i como int e igual a 0
            ; proximo arg e enquanto i < que 100000;
            o proximo arg e cada laco eu incremento i + 1 com o sinal de ++ */
            for (int i = 0; i < 100000; i++)
            {
                arrayIntLinear[i] = i;
            }

            // Crio uma matriz com [,] e instancio a ela as posicoes da matriz
            // com num int
            int[,] matriz = new int[100, 100];

            // instancio uma funcao de num randomicos
            var rand = new Random();

            // Monto dois FOR para preencher uma matriz 
            for (int i = 0; i < 100; i++)
            {
                for (int k = 0; k < 100; k++)
                {
                    matriz[i, k] = rand.Next(1, 300000);
                }
            }

            // Faco a contagem da matriz
            int countMatch = 0;

            // Este for e para contar a quantidade de linhas e colunas, onde
            // ao apontar a matriz, eu posso usar a funcao GetUpperBound(0) que 
            // me retorna a quantidade de linhas quando passo o param (0) e colunas
            // quando passo o param(1)
            for (int i = 0; i < matriz.GetUpperBound(0); i++)
            {
                for (int k = 0; k < matriz.GetUpperBound(1); k++)
                {
                    // A matriz possui uma funcao ao qual pego o valor da matriz passando
                    // as posicoes i e k, porem ela me retorna um type OBJ, entao o 
                    // (int)matriz converte o OBJ em INT
                    var valorMatriz = (int)matriz.GetValue(i, k);

                    // Agora intero em meu array para encontrar o valor em meu array:
                    // o .Length em um [] e a qtd de elementos dele
                    for (int x = 0; x < arrayIntLinear.Length; x++)
                    {
                        if (arrayIntLinear[x] == valorMatriz)
                        {
                            // Maneira de somar a variavel
                            countMatch++;
                        }
                    }
                }
            }

            Console.WriteLine($"#### Houveram {countMatch} entre vlrs randons e do array ###");
        }

        public void Exercicio2()
        {
            Console.WriteLine("######   Exercicio 02 #######");

            char[] alfabetoArray = new char[] { 'A', 'B', 'C', 'D', 'F', 'G', 'H', 'I', 'J', 'L', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Z' };
            char[] arrayCharAleatorio = new char[100];
            char[] arrayfinal = new char[100];
            Random rand = new Random();

            // Populando um array

            for (int i = 0; i < 100; i++)
            {
                // Injeto na posicao de cada i o valor de uma letra do array de alfabetoArray
                // atraves de um sorteio randomizo pela funcao radn dentro do proprio array
                arrayCharAleatorio[i] = alfabetoArray[rand.Next(0, alfabetoArray.Length)];
            }

            int posInicial = 0;
            int posFinal = 0;

            Console.WriteLine("\nInforme um valor inicial do recorte da lista de 0 a 100");

            // Converto a informacao do ReadLine que e uma str para um INT
            posInicial = int.Parse(Console.ReadLine());

            Console.WriteLine("\nInforme um valor FINAL do recorte da lista de 0 a 100");

            posFinal = int.Parse(Console.ReadLine());

            for (int i = posInicial; i < posFinal; i++)
            {
                // Escrevo os numero aleatorios 
                arrayfinal[i] = arrayCharAleatorio[i];
            }

            // Converto o array em uma STR para descompactar o array em texto
            var strale = new string(arrayCharAleatorio);
            var stringFinal = new string(arrayfinal);

            Console.WriteLine($"STR ALEATORIA SEM CONVERTER era assim: \n{arrayCharAleatorio}\n");
            Console.WriteLine($"STR ALEATORIA era assim: \n{strale}\n");
            Console.WriteLine($"STR final ficou assim: \n{stringFinal}\n");
        }
    }

}


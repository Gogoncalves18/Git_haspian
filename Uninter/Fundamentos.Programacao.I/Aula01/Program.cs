using System;
using Aula01;
// carregar a lib que possui recursos do sistema


namespace ConsoleApp.Pratica1
{
    //Sempre abro a classe assim, entre chaves
    class Program
    {
        // Guardar variavel e sempre TIPO variavel a info e ;
        char c1 = 'c';
        // Chamo uma funcao
        static void Main(string[] args)
        {
            // cmd para gerar print no terminal
            Console.WriteLine("Hello World - Aula 1");
            Console.WriteLine("---------------------");

            int int1 = 10;
            // Sempre que eu impimo uma variavel e necessario colocar $ para formatar ela
            // e joga-la dentro de {}
            Console.Write($"{int1}");
            // Outro tipos de variaveis
            bool bola1 = true;
            bool bola2 = false;

            // Dados longos eu uso o tipo LONG
            // long longos = 86234785287357123597;

            // Decimal eu preciso usar um "M" ao final do dado
            decimal decnum = 123.34M;
            // Para o float preciso folocar um "f"
            float flaaat = 234.443f;

            Console.WriteLine("---------------------");
            Console.WriteLine("Tipo de referencia");

            // Maneira de iniciar um objeto
            object homem1 = new object();

            // Ex abaixo e uma maneira mais sintetica de declarar um obj
            var homem2 = new object();

            // este exemplo mostra que o VAR nao altera o tipo do obj, ele continua 
            // sendo igual ao segundo objeto
            var homem3 = homem2;

            Console.WriteLine("Comparando Objs");
            Console.WriteLine($"{homem1.GetType().Name} | {homem3.GetType().Name} | {homem3.GetType().Name}");

            Console.WriteLine($"{homem1 == homem2}");
            Console.WriteLine($"{homem2 == homem3}");

            // STRINGs sao imutaveis, sao uma classe e sao obj ao mesmo tempo
            // se comportando como REFERENCE TYPE e as vezes VALUE TYPE

            // String com o new str ao qual eu uso uma funcao que repete 5x a letra Z
            var s1 = new string('a', 5);

            // String apartir de array de CHAR
            string s2 = new string(new char[5] { 'a', 'a', 'a', 'a', 'a' });

            Console.WriteLine($"{s1 == s2}");

            // Converter um Enumerable em string
            string s3 = string.Concat((new char[5] { 'a', 'a', 'a', 'a', 'a' }).AsEnumerable());

            var s4 = $"{s3} estamos escrevendo dentro da str junto com o s3 e s4";

            Console.WriteLine($"{s4}");

            // Compararar obj de class diferentes com o mesmo valor de str
            Console.WriteLine("###### Linha 73 #####");

            classe1 compara1 = new classe1()
            {
                testeComparacao = "123"
            };
            var compara2 = new classe1()
            {
                testeComparacao = "123"
            };

            // Esta comparacao vai dar falso pq sao 2 obj diferentes
            Console.WriteLine($"{compara1 == compara2} Comparando 2 class L86");

            // Esta comparacao deu true pq os obj sao diferentes mas foi passado para a propriedade
            // testeComparacao o mesmo valor mesmo que dentro da class havia um outro valor, como ela 
            // e publica, ela deixa escrever. Podemos comparar Int, Decimal e Enum (struct)
            Console.WriteLine($"{compara1.testeComparacao == compara2.testeComparacao} comparando propriet L91");

            Console.WriteLine($"{compara1.testeComparacao.Equals(compara2.testeComparacao)} comparando propriet L89");

            // Propriedades: podemos usar o get para recuperar o valor ou set para adicionar o valor
            // Para demonstrar, criei uma class dentro da Solution chamada CLASSECOMPLEXA

            Console.WriteLine("###### Linha 98 - Imprimir prop da CLASSECOMPLEXA #####");


            // Instancio a class ClasseComplexa toda e ela trara outra INTERFACE ao qual esta herdando
            var clasComplexa = new ClasseComplexa();
            // Aqui eu seto um valor para propriedade do obj que esta dentro do Interface1.cs
            clasComplexa.PropInterface = "123";

            var interFx = clasComplexa;

            Console.WriteLine($"{interFx.PropInterface}");

            /*
            Aula de divisor entre valores levantando exception
            */

            Console.WriteLine("######    Linha 114 - EXCEPTION  #########");

            var divisorCalculadora = new DivisorCalc();

            Console.WriteLine("Digite 'S' para sair a qq momento:");
            // Maneira de definir a variavel vazia
            string valorlido = string.Empty;
            // Tipando as variaveis de entrada
            int a;
            int b;
            // Definindo um valor fixo
            string valorSaida = "S";
            // Forma de abrir o laco while, ele sempre comeca com o DO

            // Captura do VALOR A
            do
            {
                Console.WriteLine("Digite o PRIMEIRO VALOR:");
                // Capturo o valor digitado, e o INPUT do Python
                valorlido = Console.ReadLine();

                if (valorSaida.Equals(valorlido))
                    break;

                try
                {
                    // Tento converter o vlr lido para int, se ele nao conseguir
                    // levanto uma Exception
                    a = int.Parse(valorlido);
                }
                catch (Exception err)
                // Se a Exception ser levantada, executo o code abaixo
                {
                    Console.WriteLine($"Vc digitou um vlr nao valido {valorlido}. Erro: {err.Message}");
                    // Executo o comando abaixo para forcar ele a digitar algo valido
                    continue;
                }

                // Valor B

                Console.WriteLine("Digite o SEGUNDO VALOR:");
                // Capturo o valor digitado, e o INPUT do Python
                valorlido = Console.ReadLine();

                if (valorSaida.Equals(valorlido))
                    break;

                try
                {
                    // Tento converter o vlr lido para int, se ele nao conseguir
                    // levanto uma Exception
                    b = int.Parse(valorlido);
                }
                catch (Exception err)
                // Se a Exception ser levantada, executo o code abaixo
                {
                    Console.WriteLine($"Vc digitou um vlr nao valido {valorlido}. Erro: {err.Message}");
                    // Executo o comando abaixo para forcar ele a digitar algo valido
                    continue;
                }

                // RESULTADO:

                try
                {
                    // Aciono a funcao dividir de dentro do class DIVISORCALC.cs
                    var resultado = divisorCalculadora.Dividir(a, b);
                    Console.WriteLine($"Resultado:  => {resultado}");
                }
                catch (DivideByZeroException)
                {
                    Console.WriteLine("VC NAO PODE DIVIDIR POR ZERO");
                }
                // No fechamento do DO que eu entro com o WHILE
            } while (valorSaida.Equals(valorlido) == false);

        }

    }

}


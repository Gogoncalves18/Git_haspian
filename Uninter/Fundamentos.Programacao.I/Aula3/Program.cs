using Aula3;

namespace ConsoleApp.Aula3
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("\nAula Pratica de C# 3!\n");
            Console.WriteLine("\n---------------------\n");

            Console.WriteLine("LAMBDA FUNCTON EX 01\n");

            var ConvDataSTR = new PraticaComLambdas();
            ConvDataSTR.Ex1();

            Console.WriteLine("\n---------------------");

            Console.WriteLine("LAMBDA FUNCTON EX 02\n");

            var lambInumber = new PraticaComLambdas();
            lambInumber.Ex2();

            Console.WriteLine("\n---------------------");

        }
    }
}
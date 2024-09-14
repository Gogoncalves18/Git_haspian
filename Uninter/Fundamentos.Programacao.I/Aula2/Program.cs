using System;
using System.Collections.Generic;
using Aula2;

namespace ConsoleApp.Aula2
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Aula Pratica de C# 2!");
            Console.WriteLine("---------------------");

            Console.WriteLine("---------------------");
            Console.WriteLine("Array");
            Console.WriteLine("---------------------");

            // Class criada dentro da Solution
            var praticaComArrays = new PraticaComArrays();

            praticaComArrays.Exercicio1();

            praticaComArrays.Exercicio2();



            var boxing = new PraticaComFilasBoxing();
            boxing.ExercicioBoxingFilas();
            var manipulacao = new PraticaManipulacaoCollections();
            manipulacao.Exercicio4();


            var convert = new AcionamentoExtesionMethod();
            convert.Exercicio5();


        }
    }
}

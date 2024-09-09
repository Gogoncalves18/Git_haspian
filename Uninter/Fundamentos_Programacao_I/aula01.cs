using System;
// carregar a lib que possui recursos do sistema


namespace ConsoleApp.Pratica1
{
    //Sempre abro a classe assim, entre chaves
    class Program
    {
        // Guardar variavel e sempre TIPO variavel a info e ;
        char c1 = "c";
        // Chamo uma funcao
        static void Main(strig[] args)
        {
            // cmd para gerar print no terminal
            console.WriteLine("Hello World - Aula 1");
            console.WriteLine("---------------------");

            int int1 = 10;
            // Sempre que eu impimo uma variavel e necessario colocar $ para formatar ela
            // e joga-la dentro de {}
            console.Write($"{int1}");
            // Outro tipos de variaveis
            bool bola1 = true;
            bool bola2 = false;

            // Dados longos eu uso o tipo LONG
            long longos = 86234785287357123597;

            // Decimal eu preciso usar um "M" ao final do dado
            decimal decnum = 123.34M;
            // Para o float preciso folocar um "f"
            float flaaat = 234.443f;

            console.WriteLine("---------------------");
            console.WriteLine("Tipo de referencia");

            // Maneira de iniciar um objeto
            object homem1 = new object();

            // Ex abaixo e uma maneira mais sintetica de declarar um obj
            var homem2 = new object();
            var homem3 = homem2;

            console.WriteLine("Comparando Objs");
            console.WriteLine($"{homem1.gettype().name} | {homem3.gettype().name} | {homem3.gettype().name}");

            console.WriteLine($"{homem1 == homem2}");
            console.WriteLine($"{homem2 == homem3}");

        }

    }

}


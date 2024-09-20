namespace ConsoleApp.Aula4;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("\nAula Pratica 04 C#");
        Console.WriteLine("\n############################################################");
        Console.WriteLine("\n############################################################\n");



        Console.WriteLine("\n_________________________THREADS____________________\n");

        //ThreadPing Ex_Tread_01 = new ThreadPing();
        //Ex_Tread_01.StartPing();

        Console.WriteLine("\n_________________________TASKS____________________\n");

        var Ex_Task_02 = new PessoaFinder();
        Ex_Task_02.ExPessoaAsync();


        Console.WriteLine("\n############################################################\n");


    }
}

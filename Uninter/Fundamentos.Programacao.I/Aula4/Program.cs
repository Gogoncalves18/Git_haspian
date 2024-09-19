namespace ConsoleApp.Aula4;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("\nAula Pratica 04 C#");
        Console.WriteLine("\n############################################################");
        Console.WriteLine("\n############################################################\n");



        Console.WriteLine("\n_________________________THREADS____________________\n");

        ThreadPing Ex_Tread_01 = new ThreadPing();
        Ex_Tread_01.StartPing();

        Console.WriteLine("\n############################################################\n");
    }
}

namespace ConsoleApp.Aula4;

class Program
{
    /* Toda main que usa um metodo de TASK Assincrona, isto e, espera ela responder para seguir
    e necessario usar o termo "async" "Task" antes do Main, isto por ela inicializa uma Task por
    natural e so respeitara as demais TASK se elas forem declaradas ao longo do corpo da Main.
    */
    static async Task Main(string[] args)
    {
        Console.WriteLine("\nAula Pratica 04 C#");
        Console.WriteLine("\n############################################################");
        Console.WriteLine("\n############################################################\n");



        Console.WriteLine("\n_________________________THREADS____________________\n");

        ThreadPing Ex_Tread_01 = new ThreadPing();
        Ex_Tread_01.StartPing();

        Console.WriteLine("\n_________________________TASKS____________________\n");

        /* Neste caso instancio a class "PessoaFinder()" em uma variavel com o metodo construtor
        porem ainda preciso chamar o metodo da class que dara inicio as atividades. Esta class 
        "PessoaFinder()" precisa ter o "async Task" que a define como assincrona e espera uma 
        resposta das "TASKS" que estao dentro dela. Importante e instanciar em uma variavel do 
        tipo TASK pois receberei as TASKs proveniente dela, por isto do "Task Ex_Task_02"
        */

        / Task Ex_Task_02 = new PessoaFinder().ExPessoaAsync();

        // Na variavel ao qual estou recebendo da minha class "PessoaFinder", eu uso o metodo
        // da TASK para esperar a resposta delas. Importante, dentro da class eu tenho 3 TASKS
        // independentes, la eu uso um metodo "await Task.WhenAll" para esperar todas terminarem
        // so assim a minha linha abaixo deixa MAIN prosseguir

        Ex_Task_02.Wait();

        Console.WriteLine("\n_________________________TASKS EX 03____________________\n");

        Task Ex_03 = new PesquisaDirWin().Ex_03_Task();

        Ex_03.Wait();

        Console.WriteLine("\n############################################################\n");

    }
}

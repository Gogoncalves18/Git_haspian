namespace ConsoleApp.Aula5;

class Program
{
    private static ApplicationContext dbContext;

    static async Task Main(string[] args)
    {
        Console.WriteLine("\nAula Prática 05 - BD no .NET:\n");
        Console.WriteLine("---------------------------------------------------------------------\n");

        dbContext = new ApplicationContext();

        Console.WriteLine("\n>>>>>>>>> VERIFICANDO O BD <<<<<<<<<<<\n");

        // Teste de conexão
        var canConnect = await dbContext.Database.CanConnectAsync();

        // PAREI EM 2.42MIN

    }
}

internal class ApplicationContext
{
}
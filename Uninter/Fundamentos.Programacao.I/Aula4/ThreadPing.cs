using System.Net.NetworkInformation;

namespace ConsoleApp.Aula4;

public class ThreadPing
{
    private string endereco = "google.com";
    int countPing = 0;
    bool executePing = false;

    public void StartPing()
    {
        executePing = true;
        Console.WriteLine("\nDigite (S) para cancelar: ");

        // Instancio uma "Thread" na variavel threadPingger, porem dentro dos parametros da Thread
        // eu passo o metodo que inicializara os apontamento que usam a CLASS Ping() do C#
        // com isto a Thread esta unida com meu metodo.
        var threadPingger = new Thread(ExecutePing);
        // Inicio a thread com o metodo dela .Start() e ela executa meu metodo "ExecutePing()"
        threadPingger.Start();

        // Var para controle do momento de sair do programa
        var cmdSair = "S";
        // Var instanciado como uma STR vazia, no C# nao posso usar ""
        var cmd = string.Empty;

        // Quando o programa chega aqui, ele ja entrou no laco do meu metodo "ExecutePing()"
        // e ficara imprimindo os resultados do ping ate que este laco abaixo seja quebrado.
        // Neste caso a "!" inverte a expressao posterior como um resultado boleano, o resultado e
        // se o CMD for igual a "S", o resultado do "!" e FAlSE
        while (!cmdSair.Equals(cmd))
        {
            // Enquando meu metodo esta sendo executado, o console esta esperando a resposta
            // do teclado constantemente, ao sair deste laco o VAR na linha abaixo sera alterado.
            cmd = Console.ReadLine().ToUpper();
        }

        // Com a alteracao deste VAR, meu metodo "ExecutePing()" ira ser cancelado e ela ira 
        // parar de imprimir instanteamente. E entao o programa entrara no proximo laco.
        executePing = false;

        // O interessante desta linha de laco e que o "threadPingger" esta instanciando a THREAD
        // e ele por sua vez possui um metodo ".IsAlive" que retorna TRUE para dizer que a tread 
        // ainda esta em execucao.
        while (threadPingger.IsAlive)
        {
            // Mesmo apos ter encerrado o metodo "ExecutePing()", a THREAD demora para ser derrubada
            // tanto e que ela ira imprimir varias vezes a frase abaixo.
            Console.WriteLine("\nEsperando thread finalizar");
        }

        // Alguns segundos depois ela para de imprimir a frase acima e imprime esta frase quando
        // sai do laco, o que mostra a diferenca de velocidade para a THREAD ser derrubada.
        Console.WriteLine("\n%%%%%%%% THREAD Encerrada  %%%%%%%%%%%");

    }

    public void ExecutePing()
    {
        while (executePing)
        {
            Ping pingger = new Ping();
            var pingResponse = pingger.Send(endereco);


            Console.WriteLine($"Ping {countPing}: {endereco} | Status: {pingResponse.Status} - {pingResponse.RoundtripTime}ms");
            countPing++;

            // Espera de 2 segundos
            Thread.Sleep(2000);
        }
    }
}

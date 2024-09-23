namespace ConsoleApp.Aula4;

public class PesquisaDirWin
{
    public class Diretorio
    {
        public string Nome { get; set; }
        public decimal TamnhoMB { get; set; }
        public List<Arquivo> Arquivos { get; set; }
    }

    public class Arquivo
    {
        public string Nome { get; set; }
        public decimal TamnhoMB { get; set; }
    }

    public async Task Ex_03_Task()
    {
        Console.WriteLine("\nInforme uma lista de DIRETORIOS para contar os arquivos:");
        Console.WriteLine("\n>>>>>> Digite 'S' para SAIR <<<<<<");

        string dir = string.Empty;
        string cmdStop = "S";

        // Instancio um metodo construtor de uma lista com type de STR dentro dela
        var listaDIRs = new List<string>();

        do
        {
            try
            {
                dir = Console.ReadLine();

                // metodo para ler se o dir existe, se ele for falso, "!" e o contrario, ai entro do laco
                if (!Directory.Exists(dir))
                {
                    Console.WriteLine("!!!! Este DIRETORIO nao EXISTE !!!! Tente novamente:");
                    continue;
                }

                // Se der certo a leitura do DIR, ele executa a linha imediatamente abaixo
                listaDIRs.Add(dir);
            }
            catch (Exception)
            {
                Console.WriteLine("TENTE NOVAMENTE");
            };

        } while (!cmdStop.Equals(dir));


        // Instancio um OBJ do tipo LIST que recebera Diretorio que possuem tipo Arquivo de outra class
        var dirCalc = new List<Diretorio>();

        // Crio uma lista de TASK que vamos enfilerar para uma melhor controle do num de TASKS que temos
        var listaTasks = new List<Task>();

        // Para cada pasta dentro da lista de diretorio nomearei a pasta como um OBJ
        foreach (var past in listaDIRs)
        {
            // Cada pasta sera um OBJ e converterei este OBJ em uma TASK que tera a funcao dentro de LAMBDA
            // de dar nome a pasta e encontrar os arquivos e seu tamanho.
            var taskDir = new Task(async () =>
            {
                // Instacio como um OBJ PAsta
                var dirCalc = new Diretorio
                {
                    // Dou um nome para propriedade deste objeto
                    Nome = past
                };

                // Aqui leio os arquivos dentro da pasta e nao deixo o programa prosseguir ate terminar AWAIT
                var arquivos = await FindDirFilesAsync(past);

                // A var "arquivos" traz uma serie de OBJ que contem o metodo FILEINFO() que nos da propriedades que criamos
                dirCalc.Arquivos = arquivos;

                // Gravo o tamanho do DIR lendo todos os "arquivos" que e uma LIST que herdou a classe "Arquivo"
                // o lambda percorre cada item da lista pegando o tamanho que foi gravado pelo metodo "FindDirFilesAsync(past)"
                dirCalc.TamnhoMB = arquivos.Sum(a => a.TamnhoMB);

            });

            // Separo a lista de OBJ que sao enderecados para guardar cada uma das tasks
            listaTasks.Add(taskDir);
        }

        // Aguardar todas as tasks serem finalizadas para prosseguirmos
        await Task.WhenAll(listaTasks);


        Console.WriteLine("*************");
        Console.WriteLine("Processo Over");
        Console.WriteLine("*************");
    }

    public async Task<List<Arquivo>> FindDirFilesAsync(string path)
    {
        // Criar uma task para buscar arquivos, o C# nao possui uma funcao assync para buscar arquivos, 
        // aqui apenas prendemos a funcao syncrona em uma task para controlar o quando ela inicia
        var files = await Task.Run(() =>
        {
            // Metodo "Directory" e do sistema, .GetFiles para percorrer( dentro de um caminho, pegando todas palavras,
            // contruindo um enumarable com a opcao de ler subpastas )
            var fileDir = Directory.GetFiles(path, "*", new EnumerationOptions() { RecurseSubdirectories = true });
            return fileDir;
        });

        var arquivosPastas = new List<Arquivo>(files.Count());

        foreach (var f in files)
        {
            // "FILEINFO" e uma class do system que le o arquivo sem abrir ele, apenas com os metadados, passando
            // para ele o OBJ do arquivo
            var fileInfoF = new FileInfo(f);
            arquivosPastas.Add(new Arquivo
            {
                // Com o metodo instanciado, consigo buscar o nome do arquivo e o seu comprimento
                // usando o metodo de descricao de tamanho que criamos no final da pagina
                Nome = fileInfoF.Name,
                TamnhoMB = ToSize(fileInfoF.Length, SizeUnits.MG)
            });
        }
        return arquivosPastas;
    }

    public enum SizeUnits
    {
        B, KB, MG, GB, TB, PB, EB, ZB, YB
    }

    public decimal ToSize(long value, SizeUnits unit)
    {
        return Math.Round(Convert.ToDecimal((value / (double)Math.Pow(1024, (long)unit))), 2);
    }

}

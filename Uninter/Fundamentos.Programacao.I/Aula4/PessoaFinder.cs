using System.Diagnostics;

namespace ConsoleApp.Aula4;

public class PessoaFinder
{
    public async Task ExPessoaAsync()
    {
        Console.WriteLine("\nGerando 10M pessoas ....");
        // Reserva 10M espacos em um array que instancia com a classe pessoa
        var arrayPessoas = new Pessoa[10000000];

        for (int i = 0; i < arrayPessoas.Length; i++)
        {
            // Gero as propriedades para cada objeto, com nome e id com um laco FOR
            arrayPessoas[i] = new Pessoa
            {
                Id = i,
                Nome = $"Pessoa cod {i}"
            };
        }

        // Inicializacao da colecoes, dataset que guardarei os dados

        // Converte o array em uma lista independente de pessoas, para testar a velocidade de leitura
        List<Pessoa> listaPessoas = arrayPessoas.ToList();

        // Aqui esta a sacada, este metodo "HashSet" e um identificador de objetos para tornar
        // a pesquisa mais performatica. Ele esta de Pessoa pq la dentro da class Pessoa eu montei
        // um OVERRIDE em um metodo para sobreescrever o metodo "GetHashCode()", desta forma 
        // ele executa uma comparacao entre objetos e nao deixa guardar objetos iguais.
        HashSet<Pessoa> hashSetPessoas = new HashSet<Pessoa>(arrayPessoas);

        var cmdSair = "S";
        var cmd = string.Empty;

        while (true)
        {
            Console.WriteLine("\nInforme o NUM de uma pessoa de 0 a 10M: ");

            cmd = Console.ReadLine();
            if (cmdSair.Equals(cmd))
            {
                break;
            }

            // Converter o CMD de STR para INT para aproveitar na logica abaixo
            var idPessoaSolicitada = int.Parse(cmd);

            // Instancio a pessoa que eu quero que procure no exercicio
            var pessoaProc = new Pessoa()
            {
                Nome = $"Pessoa COD {idPessoaSolicitada}",
                Id = idPessoaSolicitada
            };

            // Abaixo e criado uma TASK separada com estruturas diferentes - ESTA E UM ARRAY COM FOR
            var task1 = Task.Run(() =>
            {
                // Criacao de um cronometro para medir o tempo, usando um metodo do C#
                var cron = new Stopwatch();
                cron.Start();

                for (int i = 0; i < arrayPessoas.Length; i++)
                {
                    if (arrayPessoas[i] == pessoaProc)
                    {
                        break;
                    }
                }

                cron.Stop();

                //Iniciei e parei o cronometro do sistema, agora preciso retornar o tempo
                return cron.ElapsedMilliseconds;
            });



            // Abaixo e criado uma TASK separada com estruturas diferentes - ESTA E UMA LIST COM METODO DA CLASS PESSOA
            var task2 = Task.Run(() =>
            {
                // Criacao de um cronometro para medir o tempo, usando um metodo do C#
                var cron = new Stopwatch();
                cron.Start();

                // Este e o caso que eu uso o metodo OVERRIDE da class "Pessoa", ao inves de usar um for,
                // e usado uma procura utilizando um funcao da class list e dentro dela um Lambda
                // em uma LIST que esta instanciada na Class Pessoa, onde o "p" representa cada item da list
                // e o .Equals esta usando o metodo OVERRIDE da class Pessoa para comparar com outro objeto
                // sendo comparado por ID 

                var pessoaEncontrada = listaPessoas.Find((p) => p.Equals(pessoaProc));

                cron.Stop();

                //Iniciei e parei o cronometro do sistema, agora preciso retornar o tempo
                return cron.ElapsedMilliseconds;
            });




            // Abaixo e criado uma TASK separada com estruturas diferentes - ESTA E UM HashSet COM METODO DA CLASS PESSOA
            var task3 = Task.Run(() =>
            {
                // Criacao de um cronometro para medir o tempo, usando um metodo do C#
                var cron = new Stopwatch();
                cron.Start();


                // Este e o caso que eu uso o metodo OVERRIDE da class "Pessoa", ao inves de usar um for,
                // e usado uma procura utilizando um funcao da class "HASSET" e dentro dela eu aponto apenas
                // o objeto que estou procurando, o segredo aqui e que o metodo de "GetHashCode()" que ha
                // dentro da class "Pessoa", ira comparar com a propriedade que eu der dentro do metodo
                // neste caso foi o ID.

                var pessoaEncontrada = hashSetPessoas.Contains(pessoaProc);

                cron.Stop();

                //Iniciei e parei o cronometro do sistema, agora preciso retornar o tempo
                return cron.ElapsedMilliseconds;
            });

            // Executo um WhenAll que e metodo da Task com o recurso await, ao qual ele espera 
            // todas as TASK serem executadas para depois seguir o processo.

            await Task.WhenAll(task1, task2, task3);

            Console.WriteLine($"Task 1 (Array) levou: {task1.Result}Milseg.");
            Console.WriteLine($"Task 2 (LIST) levou: {task2.Result}Milseg.");
            Console.WriteLine($"Task 3 (HASH) levou: {task3.Result}Milseg.");

        }
    }
}

public class Pessoa
{
    public int Id { get; set; }
    public required string Nome { get; set; }

    // Metodos com o OVERRIDE sao tipo de metodos que sobreescrevem metodos de suas classes
    // supriores, isto e, a classe superior precisa ter o mesmo nome de metodo, entradas e saidas.
    // E no lugar do override precisa estar escrito virtual. Assim o metodo da classe inferior
    // pode executar um codigo diferente mesmo que tenha herdado o mesmo metodo.
    // Aqui embaixo executamos a sobreescrita do metodo do sistema, o Equal(), ele recebe um 
    // obj, valida se e nulo, depois se nao da class pessoa e se passar, entao ele valida se o ID
    // que eu estou dando da pessoa e igual ao ID do obj pessoa que ele esta comparando.
    public override bool Equals(object? obj)
    {
        if (obj == null)
        {
            return false;
        }
        if (obj is not Pessoa)
        {
            return false;
        }
        return ((Pessoa)obj).Id == Id;
    }

    // Neste caso eu sobreescrevo o metodo GetHashCode(), onde retorno apenas o ID
    public override int GetHashCode()
    {
        return Id;
    }
}

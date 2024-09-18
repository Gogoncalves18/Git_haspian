using System.Data.Common;
using System.Security.Cryptography.X509Certificates;
using System.Text;

namespace Aula3;

public class PraticaComExecucaoTardia
{
    public void Ex_Tard_01()
    {
        // Lista de objetos
        string[] produtos = new string[] { "Notebook", "Mouse", "Teclado", "Monitor", "Fonte", "Fone", "HDMI", "MousePad", "Cadeira", "Caderno", "Caneta" };
        var pessoas = new List<Pessoa>(5000);
        var rand = new Random();

        // Gera os objetos que abstrai de pessoa 
        for (int i = 0; i < 5000; i++)
        {
            pessoas.Add
            (
                new Pessoa
                {
                    Id = i,
                    Nome = $"Individuo Num {i}",
                    Pedidos = new Dictionary<int, Pedido>()
                }
            );
        }

        // Gera 50000 pedidos

        var pedidos = new List<Pedido>(50000);
        for (int i = 0; i < 50000; i++)
        {
            var produto = produtos[rand.Next(0, 11)];
            var qtdPagamentos = rand.Next(1, 3);
            var pagador = pessoas[rand.Next(0, 5000)];
            var pedido = new Pedido()
            {
                Id = i,
                Data = new DateTime(rand.Next(2019, 2025), rand.Next(1, 13), rand.Next(1, 28)),
                Produto = produto,
                Pagamentos = new List<Pagamento>(qtdPagamentos)
            };

            pagador.Pedidos.Add(pedido.Id, pedido);
            pedidos.Add(pedido);

            for (int k = 0; k < qtdPagamentos; k++)
            {
                var recebedor = pessoas[rand.Next(0, 5000)];
                // Metodo interno para gerar uma hashID unica
                var IdTransacao = Guid.NewGuid();

                var pagamento = new Pagamento
                {
                    Pagador = pagador,
                    Recebedor = recebedor,
                    IdTransacao = IdTransacao,
                    Valor = decimal.Parse($"{rand.Next(1, 10000)},{rand.Next(0, 99)}")
                };

                pedido.Pagamentos.Add(pagamento);
                pedido.ValorPedido += pagamento.Valor;
            }
        }

        // Query 1

        /*
        - Nesta query estamos assumindo a LIST pessoas e fazendo um agrupamento atraves 
        de um construtor anonimo, este OBJ tera as propriedades Pessoa, Valor e QtdPedidos.

        */
        var queryPessoasComMaiorRecebimento = pessoas.GroupBy(p => new
        {
            Pessoa = p,
            // O ped representa o pedido dentro de uma LIST pedidos que pertencem a um Individuo representado pelo OBJ.
            // Quando leio o PED da lista, o .VALUE que e um metodo interno, busca o valor
            // da propriedade ".ValorPedido" que esta na classe PEDIDO
            Valor = p.Pedidos.Sum(ped => ped.Value.ValorPedido),
            // Conta a qtd de pedidos da lista, referente a pessoa
            QtdPedidos = p.Pedidos.Count()
        })
                                                        .OrderByDescending(x => x.Key.Valor)
                                                        .FirstOrDefault();

        // Query 2

        var query2 = queryPessoasComMaiorRecebimento.Pessoa
                                                        .Pedidos
                                                        .GroupBy(x => x.Value.Produto)
                                                        .Select(x => new
                                                        {
                                                            Produto = x.Key,
                                                            Valor = x.Sum(g => g.Value.Pagamentos.Select(p => p.Valor).Sum())
                                                        }).take(5);

    }



    public class Pessoa
    {
        public int Id { get; set; }
        public string Nome { get; set; }
        public Dictionary<int, Pedido> Pedidos { get; set; }

        public override bool Equals(object obj)
        {
            if (obj == null)
                return false;

            if (obj is not Pessoa)
            {
                return false;
            }

            return ((Pessoa)obj).Id == Id;
        }

        public override int GetHashCode()
        {
            return Id;
        }
    }

    public class Pedido
    {
        public int Id { get; set; }
        public DateTime Data { get; set; }
        public string Produto { get; set; }
        public decimal ValorPedido { get; set; }
        public List<Pagamento> Pagamentos { get; set; }
    }

    public class Pagamento
    {
        public Guid IdTransacao { get; set; }
        public Pessoa Pagador { get; set; }
        public Pessoa Recebedor { get; set; }
        public decimal Valor { get; set; }
    }

}

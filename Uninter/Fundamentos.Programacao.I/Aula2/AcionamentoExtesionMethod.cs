namespace Aula2;

public class AcionamentoExtesionMethod
{
    // Exercicio para mostrar o como usar uma Metodo de Extensao que 
    // neste caso e o PraticaExtensionMethod.cs, nele ha dois
    //metodos que recebem o valor nao por dentro do () mas como 
    //variavel .CHAMADA DO METODO
    public void Exercicio5()
    {
        var str1 = "123";
        var str2 = "10,0578";
        var str3 = "9000,87";
        var str4 = "010";

        Console.WriteLine($"\n------ CONVERSOES DE STR USANDO EXTENSOES ----------\n");
        Console.WriteLine($"\nSTR 1 para INTEIRO => {str1.ToInt()}");
        Console.WriteLine($"\nSTR 2 para DECIMAL => {str2.ToDecimal()}");
        Console.WriteLine($"\nSTR 3 para DECIMAL => {str3.ToDecimal()}");
        Console.WriteLine($"\nSTR 4 para INTEIRO => {str4.ToInt()}");

        // Teste do contador implementado em METODO DE EXTENSAO E GENERICO
        var arrayBase = new int[50];
        for (int i = 0; i < arrayBase.Length; i++)
        {
            arrayBase[i] = i * 10;
        }

        // Abaixo fazemos um CASTING explicito para 3 tipos de colecao
        //ao

        IEnumerable<int> enumeravel = arrayBase;
        IList<int> lista = arrayBase;
        ICollection<int> colecao = arrayBase;

        // Abaixo sabemos que "IEnumerable" e "ICollection" nao sao items qye possuem um 
        // metodo enumerable dentro deles, neste caso, com a class generica criada em 
        // PraticaExtensionMethod.cs que tambem e um "MEtodo de Extensao", podemos executar
        // uma contagem em array de elementos, sendo eles obj como o ICollection ou sendo
        // eles array, segue o exemplo sendo aplicavel:

        Console.WriteLine($"\n------ CONVERSOES DE STR USANDO EXTENSOES e METODO GENERICO ----------\n");
        Console.WriteLine($"\nContagem de um IEnumerable => {enumeravel.CounterCustom()}");
        Console.WriteLine($"\nContagem de um IList => {lista.CounterCustom()}");
        Console.WriteLine($"\nContagem de um ICollection => {colecao.CounterCustom()}");
    }
}

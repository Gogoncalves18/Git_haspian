namespace Aula01;

public class DivisorCalc : IDivisor
{
    public int Dividir(int a, int b)
    {
        // Retorno o vlr da divisao das duas variaveis de entreda
        // para quem esta invocando a funcao
        return a / b;
    }
}

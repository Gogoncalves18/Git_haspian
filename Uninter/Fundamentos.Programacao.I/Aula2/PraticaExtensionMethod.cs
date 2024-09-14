namespace Aula2;

// UM METODO DE EXTENSAO FICA DISPONIVEL PARA TODAS CLASS DENTRO DE UM PROJETO
public static class PraticaExtensionMethod
{
    // Para o metodo ser um metodo de extensao, a class
    // precisa ser STATIC e preciso usar o THIS antes do tipo
    // da variavel. Eu informo que receberei uma STR como valor
    // e a saida dele sera um INTEIRO.
    public static int ToInt(this string value)
    {
        // Conversao de str para inteiro, esta conversao deve casar 
        // com o termo colocado no nome da funcao
        return int.Parse(value);
    }

    public static decimal ToDecimal(this string minhaStr)
    {
        return decimal.Parse(minhaStr);
    }

    // Neste caso vamos construir um Contador com o metodo de extensao
    //e dentro dele vamos colocar um metodo IENUMERABLE como um metodo
    //GENERICO dentro dele. A Propria funcao sera classificada como generica.

    public static int CounterCustom<T>(this IEnumerable<T> enu)
    {
        int count = 0;
        foreach (var item in enu)
        {
            count++;
        }
        return count;
    }
}

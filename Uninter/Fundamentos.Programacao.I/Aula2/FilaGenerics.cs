namespace ConsoleApp.Aula2;

// FILA DE GENERICS Exercicio 03
public class FilaGenerics<T>
{
    private int _countInterno;
    public int Count
    {
        get { return _countInterno; }
    }
    private T[] arrayInterno;

    public FilaGenerics(int quantidade)
    {
        _countInterno = 0;
        arrayInterno = new T[quantidade];
    }

    public void Enqueue(T elemento)
    {
        arrayInterno[_countInterno] = elemento;
        _countInterno++;
    }

    public T Dequeue()
    {
        var elemento = arrayInterno[0];

        // Este recurso bloqueia o elemento para travar tudo ate que ocorra todo este processo
        lock (arrayInterno)
        {
            // Aqui ele ira mudar todas as posicoes do elemento removendo o primeiro e reposicionando os outros
            for (int i = 1; i < _countInterno; i++)
            {
                arrayInterno[i - 1] = arrayInterno[i];
            }

            _countInterno--;
        }

        return elemento;
    }

}

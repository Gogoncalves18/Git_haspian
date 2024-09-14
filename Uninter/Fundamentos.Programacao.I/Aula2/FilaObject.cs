namespace Aula2;

// FILA DE OBJETOS Exercicio 03
public class FilaObject
{
    private int _countInterno;
    public int Count
    {
        get { return _countInterno; }
    }
    private object[] arrayInterno;

    public FilaObject(int quantidade)
    {
        _countInterno = 0;
        arrayInterno = new object[quantidade];
    }

    public void Enqueue(object elemento)
    {
        arrayInterno[_countInterno] = elemento;
        _countInterno++;
    }

    public object Dequeue()
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

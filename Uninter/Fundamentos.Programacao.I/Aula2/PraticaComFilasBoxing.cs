using ConsoleApp.Aula2;

namespace Aula2;

class PraticaComFilasBoxing
{
    public void ExercicioBoxingFilas()
    {
        // Inicializa uma lista
        var FilaGenerics = new FilaGenerics<Animal>(10);
        var FilaObject = new FilaObject(10);

        // Instancia das class filhas
        var cachorro1 = new Cachorro();
        var gato1 = new Gato();

        // Instancia com box para o tipo "pai", e uma instancia parecida com a de cima
        // porem ela esta atribuindo a uma variavel chamada Animal
        Animal cachorro2 = new Cachorro();
        Animal gato2 = new Gato();

        // Instancia com box para interface, aqui as instancia sao atribuidas a uma interface
        // chamada IBarulhento
        IBarulhento cachorro3 = new Cachorro();
        IBarulhento gato3 = new Gato();

        // Add na fila
        FilaGenerics.Enqueue(cachorro1);
        FilaGenerics.Enqueue(gato1);
        FilaGenerics.Enqueue(cachorro2);
        FilaGenerics.Enqueue(gato2);
        // Aqui e necessario colocar um casting (transfer) pq o dog3 e cat3 nao
        // sao um animal, eles sao uma interface. Sendo assim posso ter um Ibarulhento sem
        // ser um animal
        FilaGenerics.Enqueue((Animal)cachorro3);
        FilaGenerics.Enqueue((Animal)gato3);

        // Ja o obj aceita qq coisa e faz o boxing
        FilaObject.Enqueue(cachorro1);
        FilaObject.Enqueue(gato1);
        FilaObject.Enqueue(cachorro2);
        FilaObject.Enqueue(gato2);
        FilaObject.Enqueue(cachorro3);
        FilaObject.Enqueue(gato3);

        // Remove da fila
        try
        {
            while (FilaGenerics.Count > 0)
            {
                // Aqui existe um casting implicito, pq todo animal herdar um Ibarulhento.
                // Instancio em animal tudo que eu tiro da fila
                IBarulhento animal = FilaGenerics.Dequeue();
                Console.WriteLine($"\nMeu Type é: {animal.GetType().BaseType.Name}. Sou um {animal.GetType().Name}. EU emito o som {animal.EmitirSom()}.\n");
            }

            while (FilaObject.Count > 0)
            {
                // Aqui existe um casting explicito, para herdar um Ibarulhento eu preciso tornar um obj em animal.
                // Instancio em animal tudo que eu tiro da fila
                IBarulhento animal = (Animal)FilaObject.Dequeue();
                Console.WriteLine($"\nMeu Type é: {animal.GetType().BaseType.Name}. Sou um {animal.GetType().Name}. EU emito o som {animal.EmitirSom()}.\n");
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"\nErro: {ex} ");
        }
    }
}

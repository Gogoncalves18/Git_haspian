# Quebra do principio de LISKOV
class Animal:
    def alimentar(self):
        print('O animal está se alimentando')


class Cachorro(Animal):
    def latir(self):
        print('O cachorro começou a latir')


class Peixe(Cachorro):
    def nadar(self):
        print('Peixe está nadando sem parar')

    '''O principio de LISKOV diz que a classe inferior deve conseguir
    subistuir sua classe pai sem que o processo pare, porém neste caso ao
    ao rodar o metodo latir, ele levanta uma excessão porque peixe não late,
    por isto que eu posso considerar que esta classe está quebrando o
    principio.
    '''
    def latir(self):
        raise Exception('Peixe não late')


def verificar_animal(animal: any):
    '''Nesta linha podemos ver que "animal.alimentar()" funciona,
    mas ao rodar o metodo "latir()", eu não tenho uma resultado
    correto'''
    # animal.alimentar()
    animal.latir()


obj1 = Animal()
obj2 = Cachorro()
obj3 = Peixe()

verificar_animal(obj1)
verificar_animal(obj2)
verificar_animal(obj3)

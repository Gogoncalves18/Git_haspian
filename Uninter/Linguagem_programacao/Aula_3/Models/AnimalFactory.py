from Models.Cat import Cat
from Models.Dog import Dog


class AnimalFactory:
    @staticmethod
    def new_animal(animal_type, age, weight, height):
        match animal_type:
            case 'dog':
                return Dog(age=age, position=0, weight=weight, height=height)
            case 'cat':
                return Cat(age=age, position=20, weight=weight, height=height)

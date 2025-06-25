from Models.AnimalFactory import AnimalFactory

new_dog = AnimalFactory.new_animal(animal_type='dog', age=1, height=10, weigth=20)

print(new_dog.move_x)
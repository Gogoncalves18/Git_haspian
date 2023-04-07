from modulos_carros import car #Importação do módulo com classes
car_1 = car.Car('fiat', 'Uno', 1998) #maneira que eu chamo o arquivo e depois a classe
print(car_1.descr_car())
car_2 = car.Eletr_car('cherry', 'tiggo 8 EHV', 2023) #maneira que eu chamo o arquivo e depois a classe
print(f'{car_2.descr_car()} - {car_2.bateria.descr_bat()}')
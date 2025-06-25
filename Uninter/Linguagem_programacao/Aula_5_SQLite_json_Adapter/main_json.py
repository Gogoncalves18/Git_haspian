# import json
#
# # Dados a serem salvos em um arquivo JSON
# data = {
#     "name": "Luke",
#     "age": 9,
#     "weight": 45,
#     "height": 0.8,
#     "breed": "pastor alemão",
# }
#
# # Caminho para o arquivo JSON
# file_path = "data.json"
#
# # Salvar dados em formato JSON no arquivo
# with open(file_path, "w") as json_file:
#     json.dump(data, json_file, indent=4)
#
# print("Dados salvos em JSON.")
#
# # Carregar dados de um arquivo JSON
# with open(file_path, "r") as json_file:
#     loaded_data = json.load(json_file)
#
# print("Dados carregados do JSON:")
# print(loaded_data)


import json


class Dog:
    def __init__(self, name, age, weight, height, breed):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.breed = breed


# Criando um objeto da classe Dog
dog = Dog("Luke", 9, 45, 0.8, "Pastor Alemão")

# Caminho para o arquivo JSON
file_path = "dog.json"

# Convertendo o objeto para um dicionário
dog_dict = {
    "name": dog.name,
    "age": dog.age,
    "weight": dog.weight,
    "height": dog.height,
    "breed": dog.breed
}

# Salvando o dicionário em formato JSON no arquivo
with open(file_path, "w") as json_file:
    json.dump(dog_dict, json_file, indent=4)

print("Objeto da classe Dog salvo em formato JSON.")
print("Dados salvos em JSON.")

# Carregar dados de um arquivo JSON
with open(file_path, "r") as json_file:
    loaded_data = json.load(json_file)

print("Dados carregados do JSON:")
print(loaded_data)

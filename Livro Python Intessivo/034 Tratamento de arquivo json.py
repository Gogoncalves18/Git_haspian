#Criação e abertura de dados com módulo Json
import json
numbers = [2,3,5,7,11,13] #Variavel recebe os dados que trabalharemos no json
filename = 'numbers.json' #Aqui aplicamos o nome do arquivo json
with open(filename, 'w') as f_obj: #Abrimos com o Open o arquivo e o python o cria no mesmo local com a mascara f_obj
    json.dump(numbers, f_obj) #O metodo Dump armazenda a lista de numeros no formato json dentro do arquivo filename usando os dados fo f_obj

nums = []
with open(filename) as arq_obj:
    nums = json.load(arq_obj)
    print(nums)


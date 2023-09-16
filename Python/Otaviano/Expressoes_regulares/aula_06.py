#https://www.youtube.com/watch?v=in5sYO6WMlo&list=PLbIBj8vQhvm1VnTa2Np5vDzCxVtyaYLMr&index=3
import re #Modulo para tratar expressoes regulares no python


'''
Meta caracteres : 
^ - Indica que a expressao regular começa "com" 
$ - Indica que a expressao regular termina "com"  
[^a-z] - o '^' adicionado em um conjunto passa para o python que temos qualquer coisa
        de que não seja de a-z, isto é, ele funciona como uma NEGAÇÂO para expressao
        e precisa ser no começo do conjunto

'''

print('LINHA 12')

cpf = ' cpf 002.720.555-10, do fulano'

print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))

print('\nLINHA 18')

print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', cpf))
#Neste caso com o '^$' no inicio e fim eu faço com que a expressao regular
#seja 100% respeitada, é um recurso para validar um campo por exemplo. Se 
#a expressao não for respeitada, ele retornará uma lista vazia

print('\nLINHA 27')

print(re.findall(r'[^0-9a-z]+', cpf))
# Neste caso eu estou negando os numeros, ele trará o texto em volta e 
#os pontos e virgula do cpf

print(re.findall(r'[^0-9a-z]+', cpf))



#https://www.youtube.com/watch?v=in5sYO6WMlo&list=PLbIBj8vQhvm1VnTa2Np5vDzCxVtyaYLMr&index=3
import re #Modulo para tratar expressoes regulares no python


'''
shorthands \w - ele é uma atalho para pegar todas letras e algarismo com e sem  acento
Flags, 

'''

texto = '''
João trouxe     flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.

Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de 
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso pão
de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooooo, o café tá prontinho aqui. Veeeemm"! 

Texto de @joao1982
'''

print('\nLINHA 24')

print(re.findall(r'[a-zA-Z0-9]+', texto))
# Neste exemplo "[a-zA-Z0-9]+" eu encontro todas as palavras e numeros
#mas ele não encontra as palavras com acento, como João, ele quebra a palavra
#em duas e exclui o "ã". O sinal de "+" permite que não venhamos a separar 
#letra a letra


print('\nLINHA 33')

print(re.findall(r'[a-zA-Z0-9À-ú]+', texto))
# Em outras linguagens o "À-ú" é uma forma de pegar todas as letras acentuadas

print('\nLINHA 39')

print(re.findall(r'\w+', texto))
# Com o shorthand "\w" eu consigo substituir o conjunto "[a-zA-Z0-9À-ú]"




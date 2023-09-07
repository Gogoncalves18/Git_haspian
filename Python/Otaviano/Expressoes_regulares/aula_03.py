#https://www.youtube.com/watch?v=in5sYO6WMlo&list=PLbIBj8vQhvm1VnTa2Np5vDzCxVtyaYLMr&index=3
import re #Modulo para tratar expressoes regulares no python



'''
Meta caracteres : . ^ $  \ ( )

Quantificadores : * + ? { } 
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
Né jão!
'''

# * Quantificador que representa 0 ou n repetições

print(f"LINHA 29 ===> {re.findall(r'jo*ão', texto, flags=re.I)}")
#Ele irá retornar os 4 casos, onde um deles tem vários "o"
#entre o J e ã. Veja que esta palavra na linha 21 não aparece
#os outros "o" após o último "o" de minha string. Os
#quantificadores sempre pegam o caracter ao lado esquerdo dele

# + Quantificador que representa 1 ou n repetições

print(f"LINHA 37 ===> {re.findall(r'jo+ão', texto, flags=re.I)}")
#Ele irá retornar os 3 casos, ao contrario do "*", ele aceita
#a quantidade de zero ocorrencia do caracter "0", linha 24

# ? Quantificador que representa 0 ou 1 repetições

print(f"LINHA 43 ===> {re.findall(r'jo?ão', texto, flags=re.I)}")
#Ele irá retornar os 3 casos, apenas pega as palavras que tem o 
#"o" ou não

# {} Quantificador que representa a quantidade de vezes ou min e max

print(f"LINHA 49 ===> {re.findall(r'jo{1,}ão{9,15}', texto, flags=re.I)}")
#Ele irá retornar apenas 1 ocorrencia, o primeiro conjunto de "o" ele pega
#1 ocorrencia ou "n" e o segundo conjunto de "o" ele pega qualquer quantidade até
#9 ou com maximo de 15. Se eu colocar qualquer numero abaixo de 9 ele me retornará
#o resultado, se colocar 10, ele nao acha

texto2 = 'João ama ser amado de forma amadora'

# Outra funcao do quantificador

print(f"LINHA 58 ===> {re.findall(r'ama[a-z]', texto2, flags=re.I)}")
#Neste exemplo ele encontra 2 ocorrencia da linha 55. Isto porque o 
#conjunto faz a validacao da primeira letra "d" e se der match, ele 
#parte para a proxima palavra que validará a primeira letra novamente
#neste caso ele nunca testa a letra "o"

print(f"LINHA 65 ===> {re.findall(r'AMA[a-z]*', texto2, flags=re.I)}")
#Neste caso conseguimos encontrar 3 ocorrencias com a palavra "AMA"

print(f"LINHA 68 ===> {re.findall(r'AMA[a-z]{0,2}', texto2, flags=re.I)}")
#Neste caso conseguimos encontrar 3 ocorrencias com a palavra "AMA"
#porém nos reservamos a quantida máxima de caracter, de 0 à 2
#excluindo o "RA" de "AMADORA"


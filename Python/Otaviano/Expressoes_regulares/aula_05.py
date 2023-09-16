#https://www.youtube.com/watch?v=in5sYO6WMlo&list=PLbIBj8vQhvm1VnTa2Np5vDzCxVtyaYLMr&index=3
import re #Modulo para tratar expressoes regulares no python


'''
Meta caracteres : . ^ $  \ 

Grupo e retrovisores : ( )
Grupos são para utilizados para dar um contexto completo da string
, isto é, "{bha} irá encontrar "b" "h" "a" independente da ordem
destas letras, ele valida uma por uma. Já o grupo (bha) encontrará
o ocorrencias que respeitam exatamente esta sequencia "bha".

Retrovisores são a identificação do grupo ao qual posso repetir 
na expressao, isto é, (a(bc))(h) os identificadores de cada grupo,
ou retrovisores, são contados pela abertura do parenteses:

\1 seria o grupo "abc"
\2 seria o grupo "bc"
\3 seria o grupo "h"

Desta forma eu isola áreas da string que estou minerando:
'''

texto = '''
<p>Frase 1</p> <p>Frase 2</p> <p>Frase 3</p> <div>Frase 4</div>
'''

print('LINHA 29')
print(re.findall(r'<([pdiv]{1,3})>.*?</\1>', texto))
"""
O problema aqui é que o grupo "([pdiv]{1,3})" que tem a regra
do que eu vou procurar está encontranapenas 3 ocorrencias de "P"
e 1 de "DIV", pois estou chamado o mesmo grupo em "\1"
"""

print('LINHA 37')
print(re.findall(r'(<([pdiv]{1,3})>.*?</\2>)', texto))
"""
Quando trabalho com grupo, preciso separar os argumentos em
grupos, por isto que neste caso eu isolo toda a expressao e dentro
dela isolo a minha segunda expressão e chamo ela depois. Aqui
ele irá separar em tupla o inicio e fehcamento de cada tag e 
depois mostrar o valor da segunda expressao
"""

print('LINHA 47')
print(re.findall(r'(<([pdiv]{1,3})>(.*?)</\2>)', texto))
"""
Quando eu isolo a minha terceira expressao que seria o 
conteúdo dentro da tag "(.*?)", teremos 4 tuplas que representam
as 4 tags, sendo que dentro de cada uma delas teremos 3 valores:
a tag do inicio ao fim, o grupo 2 que é a chave da expressao que
estou repetindo e no terceiro valor o grupo 3 que é o conteúdo
dentro da tag
"""

# Para imprimir todos os texto dentro de cada tag, fazemos assim:

print('LINHA 60')
infos = (re.findall(r'(<([pdiv]{1,3})>(.*?)</\2>)', texto))

for inf in infos:
    print(inf[2])

# OU usando o desempacotador

for inf in infos:
    a, b, c = inf
    print(f'Mesma Coisa = {c}')

cpf = ' cpf 002.720.555-10, do fulano'

print(f'\nLINHA 74 CPF')
print((re.findall(r'[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}', cpf)))
#Este é uma maneira padrão para encontrar o CPF usando os meta caracteres
#conjunto e quantificadores

print(f'\nLINHA 79 CPF')
print((re.findall(r'([0-9]{3}\.){2}[0-9]{3}\-[0-9]{2}', cpf)))
#Neste caso eu uso um quantificador para o grupo \1 mas ele retorna 
#apenas o "720.", isto pq ele busca o primeiro grupo, grava na memoria
#busca o segundo grupo e grava no mesmo endereco de memoria. Este é o
#comportamento do GRUPO ()

print(f'\nLINHA 86 CPF')
print((re.findall(r'(([0-9]{3}\.){2}[0-9]{3}\-[0-9]{2})', cpf)))
#Se gerarmos dois grupos, ele irá printar os dados do dois grupos.
#Mas o segundo grupo foi criado apenas paa montar um quantificador

# COMO EVITAR DE SALVAR UM GRUPO NA MEMORIA:

print(f'\nLINHA 86 CPF')
print((re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}\-[0-9]{2})', cpf)))
# COm o "?:" dentro do GRUPO 2, o python não salvará ele na memoria
#isto se comprova no print, ao qual mostra apenas o grupo 1

cpf2 = '001.003.123-233'
print(f'\nLINHA 99 - DADOS em Grupo de 3 caracter separado')
print((re.findall(r'([0-9]{3})[.|-]?', cpf2)))

print(f'\nLINHA 102 - Dados em grupo de dois valor grupo e grupo 2')
print((re.findall(r'(([0-9]{3})[.|-]?)', cpf2)))

print(f'\nLINHA 105 - Dados em grupo de tres valores grupo 1, grupo 2 e grupo 3 - expressao separado')
print((re.findall(r'(([0-9]{3})([.|-]?))', cpf2)))
#https://www.youtube.com/watch?v=in5sYO6WMlo&list=PLbIBj8vQhvm1VnTa2Np5vDzCxVtyaYLMr&index=3
import re #Modulo para tratar expressoes regulares no python



'''
Meta caracteres : . ^ $  \ ( )

Quantificadores GRID e NAO GRID ou Lazzy: * + ? 
'''

texto = '''
<p>Frase 1</p> <p>Frase 2</p> <p>Frase 3</p> <div>Frase 4</div>
'''


print(f"LINHA 17 ===> {re.findall(r'<[pdiv]{1,3}>', texto, flags=re.I)}")
#Ele irá retornar os 4 casos, 3 p e 1 div dentro das <>

print(f"LINHA 20 ===> {re.findall(r'<[pdiv]{1,3}>.*', texto, flags=re.I)}")
#Ele irá retornar 1 caso, o "." traz qualquer coisa e o quantificador "*" 
#informa para o RE que posso ter "n" quantidades de caracteres. Porém
#ele está me trazendo tudo dentro de um unico item da lista, o que está errado

print(f"LINHA 25 ===> {re.findall(r'<[pdiv]{1,3}>.*</[pdiv]{1,3}>', texto, flags=re.I)}")
'''
Ele irá retornar 1 caso, isto pq esta expressao é ambigua, isto é, 
o ".*" permitem que ela tenha um comportamento GRID ao qual ao 
sempre aceita mais um caracter para ser avaliado até encontrar o fim
do texto. Neste caso "</[pdiv]{1,3}>" ele encontra o trecho 4x e 
somente para na última ocorrencia. Para evitar isto, eu posso usar
o "?" junto com o "*" para dizer a ele que é 0 ou 1, tranformando 
NÂO GRID, isto é, encontrou a primeira ocorrencia, armazena e procura
a próxima até o final do texto
'''

print(f"LINHA 37 ===> {re.findall(r'<[pdiv]{1,3}>.*?</[pdiv]{1,3}>', texto, flags=re.I)}")
#Nesta caso temos um comportamento NÃO GRID, guardo cada ocorrencia
#encontrada, o comportaento correto neste caso. Se usarmos o "+"
#no lugar do "*", ele iria desconsiderar os casos que não tem
#nada entre este espaço ">.+?<"




#https://www.youtube.com/watch?v=wBI0yv2FG6U&list=PLbIBj8vQhvm1VnTa2Np5vDzCxVtyaYLMr&index=1
import re #Modulo para tratar expressoes regulares no python


'''
Dentro das expressoes regulares temos os seguintes recursos:
FINDALL = encontra todas ocorrencias dentro da expressao montada
SEARCH = me retorna a primeira ocorrencia e qual indice encontrou
SUB = é para substituir as ocorrencias encontrada na expressao
COMPILE = é para reutilizar a expressao para eu nao ter que reescreve-la
para não ter que recompila-la sempre que precisar
'''

texto = 'Este é um teste de expressão regular dentro'

#Ele procura a palavara teste dentro da variavel texto. Neste caso o 
#R'' serve para eu nao ter que usar mais de uma \ para escapar um
#caracter quando isto faz parte da expressao regular. 
#Como resultado ele me tratar uma resposta MATCH com a palavra encontrada
# e sua posicao, como este caso: 
# <re.Match object; span=(10, 15), match='teste'>
print(re.search(r'teste', texto))

#Neste caso ele me traz uma lista com as palavras encontradas
print(re.findall(r'teste', texto))

#Aqui ele trocará a palavra TESTE por ABC no texto, com 
#parametro COUNT=1 ele trocará somente a primeira palavra 
#encontrada
print(re.sub(r'teste', 'ABC', texto, count=1))

#Abaixo uma maneiro para não repetir a compilação da 
#expressao regular e melhor a performance do comando:

#Estancio a expressao e apenas defino em que texto que
#ela deverá ser aplicada

expressao = re.compile('teste')

print(expressao.search(texto))
print(expressao.findall(texto))
print(expressao.sub('ABC', texto))
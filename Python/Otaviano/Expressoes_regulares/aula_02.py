#https://www.youtube.com/watch?v=in5sYO6WMlo&list=PLbIBj8vQhvm1VnTa2Np5vDzCxVtyaYLMr&index=2
import re #Modulo para tratar expressoes regulares no python


'''
Meta caracteres : . ^ $ * + ? { } [ ] \ | ( )
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

# | significa OU

print(f"LINHA 25 ===> {re.findall(r'João|Maria', texto)}")
#Ele irá retornar com sensecase, preservando maiscula ou minuscula

# . significa qualquer caracter com excesão da quebra de linha, a não ser que use flag
print(f"LINHA 29 ===> {re.findall(r'João|M...a', texto)}")
# Aqui reservo 3 caracteres entre M e A e ele entrontrará o mesmo padrão

# [] significa um conjunto de caracteres
print(f"LINHA 33 ===> {re.findall(r'[Jj]oão|[A-Z]...a', texto)}")
# Aqui encontro os dois joão que contem 'J e j', assim como posso abrir um 
# range de letras como no caso da letra 'M' de maria, case sensitive

# FLAGS para tratar situações na string
print(f"LINHA 38 ===> {re.findall(r'jOãO|mARia', texto, flags=re.I)}")
# Este caso com a FLAGS=re.I, ele ignora o sensitive case da string
# que estou passando

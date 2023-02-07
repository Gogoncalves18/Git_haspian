#COMO BUSCAR O ULTIMO NOME DE UMA STR DE COMPRIMENTO VARIADO
print ('-_-'*30)
name = str(input('\nEscreva seu nome completo: ')).strip()
lst = name.split()
print (name)
print ('{}.Obrigado!'.format(lst[len(lst)-1]))
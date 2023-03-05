def titulo(til):
    print('-'*50)
    print(f'{til:^60}')
    print('-'*50)


def soma(a,b):
    print(f'A = {a} e B = {b}')
    s=a+b
    print(s)


def contador(*num): #O * permite definir para o Python que eu receberei varios parametros
    print(f'Recebido uma qtd de dados que é {type(num)}')
    print(f'Comprimento do elemento é {len(num)}')
    for v in num:
        print(f'Valor = {v}')


def dobra(lst):
    print(f'Tratamento da lista {lst}')
    for pos, v in enumerate(lst):
        print(f'Valor na posicao {pos} = {lst[pos]}', end=' ')
        lst[pos]*=2 #Estou dobrando cada valor
        print(f'Ao qual dobrarei para {lst[pos]}')
    print('-'*20)
    print(f'A mesma lista ficou {lst}')


def dobra2(lst):
    lst2=[]
    print(f'Tratamento da lista {lst}')
    lst2=lst.copy() #Desreferenciando a lista
    for pos, v in enumerate(lst2):
        print(f'Valor na posicao {pos} = {lst2[pos]}', end=' ')
        lst2[pos]*=2 #Estou dobrando cada valor
        print(f'Ao qual dobrarei para {lst2[pos]}')
    print('-'*20)
    print(f'A lista da funcao ficou {lst2}')
    

#PROGRAMA PRINCIPAL:

#Para uso de funcoes, recomendasse colocar no inicio do programa e PULAR 2 linhas para iniciar o programa principal
titulo('AULA de FUNCAO')

#entrada de parametros:
print('LINHA 17')
soma(4,3)
print('LINHA 19')
soma(b=4, a=3)

#Empacotar parametros
print(f'\nLINHA 31')
contador(2,8,63,4,2)

#Tratamento de lista em funcao
lst_val=[2,6,4,8] # Lista original
print(f'\nLINHA 49 e 50')
dobra(lst_val) #lista retrabalhada pela funcao
print(lst_val) #lista original que acabou sendo impactada pela funcao porque o objeto ficou referenciado

#Tratamento de lista em funcao sem referenciar os objetos de uma lista para outra
lst_val2=[2,6,4,8] # Lista original
print(f'\nLINHA 55 e 56')
dobra2(lst_val2) #lista retrabalhada pela funcao
print(f'A lista original manteve {lst_val2}') #lista original que acabou sendo impactada pela funcao porque o objeto ficou referenciado

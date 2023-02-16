#Solicite numeros para o usuario ate que ele decida quando para
#este numero devem estar em uma lista
#nao pode haver numero repetido na lista 
#deve apresentar a lista em ordem crescente

lista_num=[]
cont_p = 's'
while cont_p == 's': #While para travar o programa em um loop
    if len(lista_num) == 0: #pego o comprimento da lista, se ela esta zerada eu ja insiro o primeiro valor
        lista_num.append(int(input('\n\033[1;35mDigite um Numero Inteiro: \033[m')))
        cont_p = str(input('\n\033[1;31mQuer continuar? [S] ou [N]\033[m ')).lower()[0] #pergunto se continuo ou interropo, pego so letra minuscula e apenas a primeira letra do teclado
    else: #aqui rodo quando eu ja tenho uma entrada na lista
        num = (int(input('\n\033[1;35mDigite um Numero Inteiro: \033[m')))
        while num in lista_num: #se o numero de entrada ja tiver na lista, fico em looping ate que seja um numero #
            num = (int(input('\n\033[1;35mTEM QUE SER UM N DIFERENTE: \033[m')))
        lista_num.append(num) #sai do looping e inseri o numero na lista           
        cont_p = str(input('\n\033[1;31mQuer continuar? [S] ou [N]\033[m ')).lower()[0]
print(f'\nLista de numeros digitados => \033[1;33m{lista_num}\033[m')
lista_num.sort()
print(f'\nPorem o software organizou sua lista => \033[1;36m{lista_num}\033[m')
    
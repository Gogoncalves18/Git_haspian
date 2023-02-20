#Criar uma lista de 5 numeros colocando em ordem crescente
#sem usar a funcao sort()
ns=[]
while len(ns) < 5: #valido se o comprimento da lista nao chegou em 5
    n=int(input('\nDigite um NUMERO: ')) #entrada de vlr
    if len(ns) == 0: #Valido se é o primeiro numero de entrada, se for, executo
        ns.append(n)
    else:
        for i in ns: #rodo a lista existente
            print(i)
            if n < i: #minha referencia é sempre encontrar qual o primeiro numero maior e inserir
                pos=ns.index(i) #Guardo a posicao para usar no insert, ele nao aceita outra sintaxe
                ns.insert(pos,n)
                break #Tenho que quebrar o FOR para incrementar no While, senao fico em looping infinito
            elif ns.index(i)+1 == len(ns) and n > i: #Regra para saber se é o ultimo numero que estou interando
                print(i)
                ns.append(n) #Como é o ultimo numero, apenas insiro pq ele sempre entra por ultimo
                print(ns[ns.index(i)])
                break #Tenho que quebrar o FOR para incrementar no While, senao fico em looping infinito
            else:
                continue
print(f'Segue a lista => {ns}')

            

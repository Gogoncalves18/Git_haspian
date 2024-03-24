# Apresentar uma lista de produto e preco que esta dentro de um tupla
# porem o print tem que sair tabulado

list_prod = ('Sabao', 'R$27.00', 'Arroz', 'R$10.45', 'Feijao',
             'R$3.45', 'Carne', 'R$32.86', 'Batata', 'R$14.45',
             'Batata Doce Inglesa', 'R$13.50')
cont_vlr = 1
# contador incremental para jogar o id uma posicao para frente,
# pulando de produto para preco
for id in range(0, (len(list_prod))-1):
    # range ajustado para uma posicao a menos para casar com 0
    if id < (len(list_prod)-1) and id % 2 == 0:
        # valido se o id e menor que o comprimento da lista e leio
        # apenas posicao pares
        print(f'''{list_prod[id]:<} {"-"*(25-len(list_prod[id]))}
              {list_prod[id + cont_vlr]}''')
        # para apresentar o preco, coloco uma posicao a mais para
        # garantir que nao estou lendo o produto

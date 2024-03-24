saca_din = int(input('\nQual o valor que deseja sacar R$: '))
ced_2 = 0
ced_5 = 0
ced_10 = 0
ced_50 = 0
ced_100 = 0
rest_din = saca_din  # Preservo o valor solicitado para fazer todas as\
# OPs com o rest_din
while rest_din != 0:  # Enquanto nao executar todas as operacoes ate
    # zerar o rest_din, o programa fica achando o divisor
    if rest_din >= 100:  # atuo somente em notas acima de 100
        res_op = int(rest_din/100)
        # Pego o resultado inteiro da divisao por 100
        rest_din = rest_din-(res_op*100)
        # calculo o resto que sobrou e gravo na variavel rest_din
        ced_100 += res_op
        # Adiciono a divisao inteira ao contador de cedulas
        rest_din = rest_din % 100
        # gravo o valor do resto na varialvel como o ultimo valor
        print(f'{ced_100} nota de R$100')
    elif rest_din >= 50 and rest_din < 100:
        # Daqui para baixo so repete a logica de cima com valores
        # menores ate chegar o rest_din igual a zero
        res_op = int(rest_din/50)
        rest_din = rest_din-(res_op*50)
        ced_50 += res_op
        rest_din = rest_din % 50
        print(f'{ced_50} nota de R$50')
    elif rest_din >= 10 and rest_din < 50:
        res_op = int(rest_din/10)
        rest_din = rest_din-(res_op*10)
        ced_10 += res_op
        rest_din = rest_din % 10
        print(f'{ced_10} nota de R$10')
    elif rest_din >= 5 and rest_din < 10:
        res_op = int(rest_din/5)
        rest_din = rest_din-(res_op*5)
        ced_5 += res_op
        rest_din = rest_din % 5
        print(f'{ced_5} nota de R$5')
    elif rest_din >= 2 and rest_din < 5:
        res_op = int(rest_din/2)
        rest_din = rest_din-(res_op*2)
        ced_2 += res_op
        rest_din = rest_din % 2
        print(f'{ced_2} nota de R$2')
    elif rest_din < 2:
        # Se o resto nao for divisivel por 2, a menor nota, cancelo a operacao.
        print(f'Nao é possível retirar o valor de {saca_din}')
        break

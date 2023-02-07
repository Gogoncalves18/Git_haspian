#Desevolva um programa que leia nome, idade e sexo de 4 pessoas. No final,
#mostre um resumo com media de idade do grupo, quantas mulheres tem menos
#que 20 anos e qual o nome e idade do homem mais velho
idade_media = int(0)
h_velho = int()
f_menos_20_anos = int(0)
for n_person in range(1,5):
    nome = str(input('\nNome da pessoa: ')).title()
    #TESTE DENTRO DE WHILE PARA TER CERTEZA QUE A ENTRADA RESPEITOU
    #O PADRAO DE NUMERO INTEIRO
    while True:
        try: #TENTO RECEBER A IDADE
            idade = int(input('Insira a idade: '))
        except ValueError: #SE ELE VOLTAR COM ERRO POR NAO SER INT, EU EXECUTO
            print('POR FAVOR, ENTRE COM APENAS NUMEROS!')
            continue
        else: #CASO CONTRARIO, SIGO O CODIGO
            idade_media += idade
            break
    while True: #TESTE A ENTRADA SE E M OU F
        sexo = str(input('Insira o sexo da pessoa, "M" para homens e "F" para mulheres: ')).upper()[0]
        if sexo == 'M' or sexo == 'F':
            if sexo == 'M':
                if idade > h_velho:
                    h_velho = idade
                    nome_mais_velho = nome
            else:
                if idade < 20:
                    f_menos_20_anos += 1
            break
        else:
            print('Por favor, insira M ou F para instrucao Sexo!')
            continue
    print('''\nDados Inseridos:
    {}
    {} Anos
    Sexo {}'''.format(nome, idade, sexo))
print('\nResumo dos dados inseridos: ')
print ('\nA media de idade do grupo e de {} Anos!'.format(idade_media/n_person))
print('\nO homem mais velho e {}, com idade de {}anos.'.format(nome_mais_velho,h_velho))
print('\nNeste grupo ha {} mulheres com idade menor que 20 anos.'.format(f_menos_20_anos))
    
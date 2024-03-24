"""Programa para ler cadastro de idade e sexo de varias pessoas. A cada pessoa
ele deve perguntar se quer continuar. No final preciso mostrar um resumo com:
quantos sao maior de idade, quantos homens e quantas mulheres sao menor.
"""
print('\n\033[1;30;42m{:<16}{:^30}{:>16}\033[m'
      .format('-_-'*15, ' CADASTRO DE PESSOAS ', '-_-'*15))
sexo = ''
idade = 0
sair_prog = False  # flag para sair do programa
maior_18 = 0  # contador acima de 18 anos
menor_18 = 0  # contador abaixo de 18 anos
h_s = 0  # contador de homens
m_s = 0  # contador de mulheres
while True:
    if sair_prog is False:
        print("")
        while True:  # teste para validar a entrada de idade apenas em numero
            try:
                idade = int(input('Qual a idade: '))
            except ValueError:
                print('Digite apenas um valor inteiro numeral!')
            else:
                break
        while True:  # Teste para validar o sexo
            sexo = str(input('Sexo [M] ou [F]: ')).upper()[0]
            if sexo not in 'MF':
                print('Digite apenas \033[1;32m{}\033[m ou \033[1;32m{}\033[m'
                      .format('M', 'F'))
            else:
                resp_saida = str(input('\nVc quer continuar? \
                [S] ou [N]')).upper()[0]
                while resp_saida not in 'SN':
                    resp_saida = str(input('\nDIGITE [S] ou [N]')).upper()[0]
                if resp_saida == 'N':
                    sair_prog = True
                    resp_saida = 'N'
                    resp = str('passei pelo NAO')
                elif resp_saida == 'S':
                    sair_prog = False
                    resp_saida = 'S'
                    resp = str('passei pelo SIM')
            break
        #
        if idade == 0:
            print('ERRO!!!!!!!')
        elif idade >= 18:
            maior_18 += 1
            if sexo == 'M':
                h_s += 1
        elif idade < 18 and idade != 0:
            if sexo == 'F':
                menor_18 += 1
            else:
                h_s += 1
        #
    else:
        break
print(f'''\n
    Numero de Adultos : {maior_18}
    Numero de Homens  : {h_s}
    Numero de Mulheres menor de Idade: {menor_18}
''')
print('\n\033[1;30;41m{:<16}{:^30}{:>16}\033[m'
      .format('-_-'*15, ' FIM ', '-_-'*15))
print("")

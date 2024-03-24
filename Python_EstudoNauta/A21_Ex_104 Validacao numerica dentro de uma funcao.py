'''Crie um programa que leia uma entrada de informação e aceite apenas
numero inteiro.
Qualquer outra coisa como espaço, letras e valor vazio deve ser
avisado ao usuário.
'''


def validar_num(info):  # Recebo uma informacao na funcao
    while True:  # Abro um looping para ficar validando a info
        try:
            # Abro o except tentando verificar se a info é um inteiro
            if int(info):
                print(f'\n\033[1;33;45m {info} \033[m')
                # aqui eu poderia construir um retorno
        except ValueError:
            # Se a info nao for um inteiro ele subira um tracing back
            # de ValueError
            info = input('\n\033[1;37;43mVc precisa digitar um numero \
inteiro:\033[m ')  # Peco uma nova entrada
            continue  # Continuo na validacao
        else:
            break  # Se der tudo certo, encerro o looping


# PROGRAMA PRINCIPAL
n = input('\nDigite um numero: ')
validar_num(n)

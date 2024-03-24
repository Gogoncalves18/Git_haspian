'''Programa para validar exceções da entrada de um numero inteiro
e um real'''
from Modulos_Uteis import cores

sair = False
while sair is False:
    try:
        num_int = int(input('\nDigite um numero inteiro: '))
    # except Exception as erro:
        # print(f'O tipo de erro foi {erro.__class__}')
    except ValueError:
        cores.titulo('Você não digitou um numero inteiro', 1)
    except KeyboardInterrupt:
        cores.titulo('Usuario abortou o programa.', 3)
        break
    else:
        print(num_int)
        break
while sair is False:
    try:
        num_fl = int(input('\nDigite um numero real: '))
    # except Exception as erro:
        # print(f'O tipo de erro foi {erro.__class__}')
    except ValueError:
        cores.titulo('Você não digitou um numero inteiro', 1)
    except KeyboardInterrupt:
        cores.titulo('Usuario abortou o programa.', 3)
        break
    else:
        print(num_fl)
        break

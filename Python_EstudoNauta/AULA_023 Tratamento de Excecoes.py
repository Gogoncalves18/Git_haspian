a = 10
b = 2

try:
    c = a/b
except ValueError:
    print('LINHA 7 - Houve erro')
else:
    # Esta clausula é opcional e será executada somente se não ocorrer
    # exceções no programa
    print(f'LINHA 9 - {c}')
finally:
    # Esta clausula é opcional e será executada com erro ou não
    print('\nLINHA 11 - Obrigado, programa encerrado')

a = 10
b = 'tt'

try:
    c = a/b
except Exception as erro:
    ''' aqui o exception é uma classe que grava o tipo de erro na
        variavel'''
    # print(f'\nLINHA 19 - Anotação: {erro.__annotations__}')
    # print(f'\nLINHA 20 - Causa: {erro.__cause__}')
    print(f'\nLINHA 21 - Classe: {erro.__class__}')
    # # Apresenta a classe do objeto que devolveu o erro
    # print(f'\nLINHA 22 - Contexto: {erro.__context__}')
    # print(f'\nLINHA 23 - Dict: {erro.__dict__}')
    # print(f'\nLINHA 24 - Delattr: {erro.__delattr__}')
    # print(f'\nLINHA 25 - Doc: {erro.__doc__}')
    # # Traz uma explicação mais explicita e didatica do erro
    print(f'\nLINHA 26 - Repr: {erro.__repr__}')
    print(f'\nLINHA 27 - Sizeof: {erro.__sizeof__}')
    print(f'\nLINHA X - Anotação: {erro}')
else:
    print(f'LINHA 29 - {c}')
finally:
    print('\nLINHA 31 - Obrigado, programa encerrado')

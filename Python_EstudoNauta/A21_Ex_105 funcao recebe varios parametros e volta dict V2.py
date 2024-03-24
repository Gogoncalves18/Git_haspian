'''Faça um programa que tena uma função notas() que receba
um numero de notas indeterminada e retorne um DICT com as
seguites infos:
- Quantidades de notas
- Maior nota
- A menor nota
- A media da turma
- A situação que deve ser opcional
- Adicione um docstring para explicar a função
'''


def notas(*n, sit=False):
    # Linha abaixo com """ é uma Docstring para a função
    """Esta função poderá trabalhar com:
        - n entrada de notas, ela avaliará a maior nota, a menor e a
          media da turma, assim como a qtd de notas
        - no final da função o recursos sit poderá dar a situação da
          turma, se é ruim ou boa perante media 6
        - sit=False, ela não irá imprimir a situação
        - sit=True, ela imprime a situação
    """
    aval_notas = {}
    aval_notas['qtd_notas'] = len(n)
    aval_notas['mai_nota'] = max(n)
    aval_notas['men_nota'] = min(n)
    aval_notas['med_nota'] = sum(n)/len(n)
    if sit is False:
        # Defino o como executarei o print de acordo com a variável
        # "sit" que será preenchida
        print(f'\n {aval_notas}')
    else:
        if aval_notas['med_nota'] < 6:
            print(f'\n {aval_notas} : OBS.: A Situação da turma é Ruim')
        else:
            print(f'\n {aval_notas} : OBS.: A Situação da turma é BOA')


# PROGRAMA PRINCIPAL
notas(3, 2, 7)
notas(6, 8, 9, 7, 8, sit=True)
notas(3, 3, 2, 3, 5, 7, 5, 7, sit=True)
# help(notas)

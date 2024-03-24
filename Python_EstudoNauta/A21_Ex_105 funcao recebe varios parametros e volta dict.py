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
    nota_m = 0
    nota_men = 0
    soma_notas = 0  # Todas variáveis acima para zeramento
    aval_notas = {'qtd_notas': 0, 'mai_nota': 0, 'men_nota': 0,
                  'med': 0}  # Montagem de um Dict pré formatado
    for i in range(0, len(n)):
        # Aqui eu executo loopings onde i é o numero de interação do
        # looping e n é a quantidade de numeros que entraram na função
        soma_notas += n[i]
        # Aqui eu leio a primeira nota da tupla sendo "n" o valor e
        # "i" a posição da tupla
        if i == 0:
            # Se for o primeiro giro, coloco o primeiro valor em menor
            # e maior valores
            aval_notas['mai_nota'] = n[i]
            aval_notas['men_nota'] = n[i]
            nota_m = nota_men = n[i]
        else:
            # Aqui preencho ou o maior valor ou o menor dependento
            # do valor que estou lendo em "n[i]"
            if nota_men > n[i]:
                aval_notas['men_nota'] = n[i]
                nota_men = n[i]
            elif nota_m < n[i]:
                aval_notas['mai_nota'] = n[i]
                nota_m = n[i]
    aval_notas['qtd_notas'] = len(n)
    aval_notas['med'] = soma_notas/len(n)
    if sit is False:
        # Defino o como executarei o print de acordo com a variável
        # "sit" que será preenchida
        print(f'\n {aval_notas}')
    else:
        if aval_notas['med'] < 6:
            print(f'\n {aval_notas} : OBS.: A Situação da turma é Ruim')
        else:
            print(f'\n {aval_notas} : OBS.: A Situação da turma é BOA')


# PROGRAMA PRINCIPAL
notas(2, 8, 4, 7, sit=True)
help(notas)

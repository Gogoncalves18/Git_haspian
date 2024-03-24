'''Programa que leia nome, sexo e idade de varias pessoas.
Guarde os dados de cada pessoa em um DICT e os DICTS
em uma lista. No final apresente:
-Quantas pessoas cadastradas
-Media de idade do grupo
-Quais sao mulheres
-Uma lista com idade acima da media
Obs.: Necesario validar a entrada de sexo e continuacao
'''
inf_p = {}  # informacoes de cada pessoa
lst_ps = []  # Lista contendo dicionario de varias pessoas
while True:  # Looping para quando a variavel SAIR for S
    inf_p['nome'] = str(input('\nNome: '))
    while True:  # Validacao da idade com controle de excesao
        try:
            inf_p['idade'] = int(input('\nIdade: '))
        except ValueError:
            print('Por Favor, informe apenas NUM para idade!')
        else:
            break
    inf_p['sexo'] = 'a'  # Setagem do sexo apenas para fazer o
    # controle de entrada do valor
    while inf_p['sexo'] not in 'MF':  # Validaao da resposta apenas
        # em M ou F
        inf_p['sexo'] = str(input('Sexo [M] ou [F]: ')).upper()[0]
    lst_ps.append(inf_p.copy())  # Armazenamento dos DICTS em lista
    sair = 'a'  # Variavel para controle de saida do programa
    while sair not in 'SN':  # Validacao da resposta de saida do programa
        sair = str(input('Finalizar os dados? [S] ou [N]')).upper()[0]
        # Sair do programa
    if sair in 'S':
        break
print('-:'*30)
print(f'\nLista da pessoas => {lst_ps} pessoas.')  # lista Bruta
print(f'\n{("<")*30} RESUMO {("<")*30}')
print(f'\nForam cadastradas {len(lst_ps)} pessoas.')
idade_med = num_m = 0  # Variaveis de controle estatistico para media
# de idade e numero de mulheres
p_up_med = []  # Pessoas com idade acima da media
for v in lst_ps:
    idade_med += v["idade"]  # Contagem da idade
    if v["sexo"] in 'F':
        num_m += 1  # contagem de mulheres
for v in lst_ps:
    if v["idade"] > idade_med/len(lst_ps):
        p_up_med.append(v["nome"])
        # Separacao das pessoas acima da media de idade do grupo
print(f'A media de idade do grupo é de {idade_med/len(lst_ps)} anos.')
print(f'Temos {num_m} mulher(es) no grupo.')
print(f'Temos as seguintes pessoas {p_up_med} que estao acima da media\
de idade de {idade_med/len(lst_ps)} anos.')
print(lst_ps)

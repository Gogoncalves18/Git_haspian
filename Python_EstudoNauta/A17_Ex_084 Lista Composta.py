# Perguntar o nome e idade de um numero
# inderterminado de pessoas e guarde em uma
# lista. Apos determine:
# Quantas pessoas foram cadastradas!
# Defina uma lista com a ou as pessoas mais idosas
# Defina uma lista com a ou as pessoas mais jovens
lst_p = []  # lista inicial para cadastro
lst_p_estr = []  # tratamento da lista inicial, cada pessoas é uma
# lista dentro de uma lista estruturada por nome e idade
lst_y_old = []  # Pessoas mais velhas
lst_y_young = []  # Pessoas mais jovens
sair = str()  # variavel para gatilho de saida do programa
idade_m = idade_me = 0  # inicio a idade zerada para determinar
# que é mais velho e mais novo
while sair == "N" or sair == str():  # Laço para sair do programa
    lst_p.append(str(input('\nInsira Nome: ')))
    lst_p.append(int(input('Insira Idade: ')))
    sair = str(input('\nQuer parar? [S] ou [N]')).upper()[0]
    # Transformar a saida em maiuscula e apenas a primeira letra
    while sair not in 'SN' or sair == str():
        # Validaçao para resposta de saida ficar somente em S ou N
        sair = str(input('\nDigite apenas? [S] ou [N]')).upper()[0]
        if sair == 'S':
            sair = 'S'
            break
print(lst_p)
pos = 0
# Definicao da posicao do proximo laco, para fazer um controlador
# de posicao dentro da lista
for v in lst_p:  # Varro a lista para ler cada valor
    if type(v) is str:  # Se for nome, sera uma STR, pego a variavel
        # pos e fatio a lista em uma lista estruturada
        lst_p_estr.append(lst_p[pos:(pos+2)])
        pos += 1
    else:  # O que nao é STR, sei que é idade, entao comeco a separar
        # as pessoas mais velhas das mais novas
        if idade_m == 0 and idade_me == 0:
            # Se for a primeira idade lida, jogo a mesma pessoa na lista
            # de mais velhas e novas
            lst_y_old.append(lst_p[(pos-1):(pos+1)])
            lst_y_young.append(lst_p[(pos-1):(pos+1)])
            idade_m = idade_me = v
        elif v == idade_m and v == idade_me:  # Se a segunda idade for
            # a mesma que a primeira, continuo a alimentar ambas listas
            lst_y_old.append(lst_p[(pos-1):(pos+1)])
            lst_y_young.append(lst_p[(pos-1):(pos+1)])
            idade_m = idade_me = v
        elif v >= idade_m:  # Valido somente os mais velhos
            if v == idade_m:  # se ja tenho uma idade igual ja lida,
                # apenas executo um append
                lst_y_old.append(lst_p[(pos-1):(pos+1)])
                idade_m = v
            elif v < idade_m:  # desconsidero o valor e sigo no proximo
                # laco
                continue
            elif v > idade_m:  # Se encontrei uma idade maior, deleto a
                # lista e insiro o novo valor
                del lst_y_old[:]
                lst_y_old.append(lst_p[(pos-1):(pos+1)])
                idade_m = v
        elif v <= idade_me:
            if v == idade_me:  # se ja tenho uma idade igual ja lida,
                # apenas executo um append
                lst_y_young.append(lst_p[(pos-1):(pos+1)])
                idade_me = v
            elif v < idade_me:  # Se encontrei uma idade maior,
                # deleto a lista e insiro o novo valor
                del lst_y_young[:]
                lst_y_young.append(lst_p[(pos-1):(pos+1)])
                idade_me = v
            elif v > idade_me:  # Desconsidero
                continue
        pos += 1
print(f'\nPessoas cadastras {len(lst_p_estr)} pessoas.')
print(f'\nPessoas mais velhas => {lst_y_old}')
print(f'\nPessoas mais jovens => {lst_y_young}')

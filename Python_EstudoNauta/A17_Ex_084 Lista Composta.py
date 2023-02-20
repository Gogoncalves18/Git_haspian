#Perguntar o nome e idade de um numero 
#inderterminado de pessoas e guarde em uma
#lista. Apos determine:
#Quantas pessoas foram cadastradas!
#Defina uma lista com a ou as pessoas mais pesadas
#Defina uma lista com a ou as pessoas mais leves
lst_p=[]
lst_p_estr=[]
lst_y_old=[]
lst_y_young=[]
sair=str()
idade_m=0
while sair == "N" or sair == str():
    lst_p.append(str(input('\nInsira Nome: ')))
    lst_p.append(int(input('Insira Idade: ')))
    sair=str(input('\nQuer parar? [S] ou [N]')).upper()[0]
    while sair not in 'SN' or sair==str():
        sair=str(input('\nDigite apenas? [S] ou [N]')).upper()[0]
        if sair == 'S':
            sair='S'
            break
print(lst_p)
pos=0
print(lst_p[pos:(pos+2)])
for v in lst_p:
    if type(v) is str:
        lst_p_estr.append(lst_p[pos:(pos+2)])
        pos+=1
    else:
        if v == idade_m:
            lst_y_old.append(lst_p[(pos-1):(pos+1)])
            idade_m=v
        elif v < idade_m:
            continue
        elif v > idade_m:
            del lst_y_old[:]
            lst_y_old.append(lst_p[(pos-1):(pos+1)]) 
            idade_m=v
        pos+=1
print(f'\nForam cadastras {len(lst_p_estr)} pessoas.')
print(lst_y_old)

        
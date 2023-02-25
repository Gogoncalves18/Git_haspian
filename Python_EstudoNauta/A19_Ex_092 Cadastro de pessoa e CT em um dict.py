#Programa que leia o nome, ano de nascimento
# e CT e cadastre com idade em um dict.
#Se nao tiver CT, ela nao deve receber 
#ano de contratacao e salario
#Calcule com quantos anos a pessoa vai aponsentar
import datetime
cad_p={}
ano_atual=datetime.date.today().year
while True:
    cad_p["nome"]=str(input('\nNome: '))
    cad_p["ano_nasc"]=int(input('\nQual ano de nascimento: '))
    if ano_atual-cad_p['ano_nasc'] >= 18: #Validar ser e maior de idade para ter CT
        cad_p["idade"]=(ano_atual-cad_p["ano_nasc"])
        cad_p["num_ct"]=int(input('Digite N˙ da CTPS: '))
        cad_p["ano_contrato"]=int(input('Ano da Contratacao: '))
        cad_p["salario"]=int(input('Salario registrado: '))
        cad_p["tempo_aposent"]=45-(ano_atual-cad_p["ano_contrato"])
        print(':'*60)
        for k,v in cad_p.items():
            print(f'{k} => {v} ')
        print(':'*60)
        sair=str(input('\nQuer Continuar? [S] ou [N]: ')).upper()[0]
        if sair == 'N':
            break
    else:
        cad_p["idade"]=(ano_atual-cad_p["ano_nasc"])
        sair=str(input('\nMenor de idade, quer inserir outra pessoa? [S] ou [N]: ')).upper()[0]
        if sair == 'N':
            break


print(f'\n\033[1;32m Digite quantos valores quiser, somarei eles quando vc clicar Q para sair \033[m ')
sair=False
soma=0
while sair == False:
    num=int(input("Digite um numero: "))    
    if num==999:
        sair=True
    else:
        soma+=num
        continue
print(f'Soma de todos os numeros é: {soma}') 

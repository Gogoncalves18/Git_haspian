#Encontrar o numero primo de uma entrada. Lembrando que num primo
#So e divisivel por apenas um num e ele mesmo.
num_in = int(input('Digite um numero: '))
qtd_div = int(0)
for c in range(1,num_in+1):
    vlr_div = int(num_in % c)
    if num_in % c == 0:
        qtd_div += 1
        print('\033[1;33;40m{}\033[m'.format(c), end= ' ')
    else:
        print(c, end= ' ')
if qtd_div == 2:
    print('\nNo numero digitado temos apenas \033[1;33;40m{} {}\033[m que sao primos de {}!'.format(qtd_div,'Numeros AMARELO', num_in))
else:
    print('\nNo numero digitado temos apenas \033[1;33;40m{} {}\033[m que NAO sao primos de {}!'.format(qtd_div,'Numeros AMARELO', num_in))

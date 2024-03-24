num_oi = int(0)
for c in range(0, 5):
    # lembrando que ele nao executa o ultimo numero do range.
    msg = str('Oi {}!'.format(num_oi))
    num_oi += 1
    print(msg)

# Outro exemplo
for c in range(0, 5):
    print(c)

# Outro exemplo porem com contagem regressiva
for c in range(5,   0,  -1):
    print(c)

# Definir o range no programa
qtd_range = int(input('Quantos intervalos devo gerar? '))
for c in range(0, qtd_range):
    print(c)

# Exemplo de while
resp = 'S'
while resp in 'Ss':
    num = int(input('Digite:  '))
    resp = str(input('Quer continuar? [S-N] ')).upper().strip()[0]

# Exemplo de .

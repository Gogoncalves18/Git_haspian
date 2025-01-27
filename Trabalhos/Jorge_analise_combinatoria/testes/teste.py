from valida_par_impar import validar_par_impar

jogo = (1, 2, 3, 4, 5, 11, 12, 13, 14, 15)

'''VARIAVEIS'''
# Numero de combinacoes por linha <<<<<<<<<<<<<<<
#comb = 5  # <<<<<<<<<<<<<<
max_seq_diagonal = 3  # <<<<<<<<<<<<<<
qtd_num_por_resultado = 10 # <<<<<<<<
num_inicial_para_combinar = 1 # <<<<<<<<
num_final_para_combinar = 21 # <<<<<<<<
# Valor "qtd_de_seq = 1" para 1 sequencia ou 2 numeros em sequencia
qtd_de_seq = 3  # <<<<<<<<<<<<<<

# Dict para armazenar por linha os resultados da combinacao
res = {}
# Qtd de numeros para o jogo
lim = 100
# Lista de numero para combinacao
lst_num = []
# Nomes para coluna do DF
coluns = []
# Numeros por linha do jogo para ser combinado
linJ = {}

# Qtd de colunas no jogo
col = 5
# Criacao de lista que formara coluna dos resultados
for c in range(1, col+1):
    coluns.append('Col_' + str(c))
coluns.append('LinJ')

# Criacao da lista
cont = 1
linha = 0
for i in range(1, lim+2):
    if cont < 11:
        cont += 1
        lst_num.append(i)
    elif cont > 10:
        linha += 1
        cont = 2
        linJ[linha] = lst_num
        lst_num = []
        lst_num.append(i)
# numero de jogadas validas
possib = 0
lin = 0

validacao_par_impar_seq = validar_par_impar(jogo, linJ, possib)
if validacao_par_impar_seq == 0:
    pass
else:
    print(validacao_par_impar_seq)
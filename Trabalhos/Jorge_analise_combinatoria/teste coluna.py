from valida_coluna import validar_coluna
jogo = (1, 2, 3, 5, 7, 11, 16, 18, 19, 20, 23, 24, 26, 27, 29, 32, 34, 37, 38, 40, 42, 43, 45, 47, 50, 51, 54, 55, 58, 59, 61, 62, 63, 68, 69, 71, 74, 75, 76, 80, 82, 84, 86, 87, 88, 93, 95, 96, 99, 100)

#jogo = (1, 2, 3, 4, 10, 16, 17, 18, 20)

'''VARIAVEIS'''
# Numero de combinacoes por linha <<<<<<<<<<<<<<<
#comb = 5  # <<<<<<<<<<<<<<
max_seq_diagonal = 3  # <<<<<<<<<<<<<<
qtd_num_por_resultado = 10 # <<<<<<<<
num_inicial_para_combinar = 1 # <<<<<<<<
num_final_para_combinar = 21 # <<<<<<<<
# Valor "qtd_de_seq = 1" para 1 sequencia ou 2 numeros em sequencia
qtd_de_seq = 4  # <<<<<<<<<<<<<<
qtd_coluna_por_res = 5  # <<<<<<<<<<<<<<

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

validacao_coluna = validar_coluna(jogo, qtd_coluna_por_res, possib, linJ)
if validacao_coluna == 0:
    print('eerooo')
else:
    print(validacao_coluna)
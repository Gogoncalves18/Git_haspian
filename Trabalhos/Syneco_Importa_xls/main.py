from conex_db import cons_sql
from df_dados import df_xls
import pandas as pd
from atualiza_excel import confirma_importacao


# Busca as OPs que ja existem no BD
k_op = cons_sql()
# Variavel com OPs que ja existem
list_op = []
ops_to_excel = []
list_ops_to_update = []
list_ops_to_del = []

# Tratamento diferente se nao ha nada no BD e se ha dados
if k_op == []:
    # Descompacta em duas variaveis, o DF do que foi para BD e
    # 0 ou 1 se ocorreu insucesso ou sucesso no BD
    df, dados = df_xls(list_op)
    # Instancio o DF para facilitar
    df_inserted = pd.DataFrame(df)
    # Separa apenas as OPS novas que foram para o BD para flag no excel
    ops_news_excel = df_inserted['OP']
    # Cria uma lista de controle de quais ops devem ser atualizadas no Excel
    for op in ops_news_excel:
        ops_to_excel.append(op)

    # Condicional para somente atualizar no excel se realmente ter ocorrido
    # a atualizacao em BD
    if dados == 1:
        confirma_importacao(ops_to_excel)
    else:
        print('Erro 1001 - Insert no BD')
else:
    # Varre o comprimento de resultados provenientes do BD
    for k in range(0, len(k_op)):
        # Cria uma lista de controle fatiando apenas as OP's,
        # cada linha em K para a coluna 1 que e a OP
        list_op.append(k_op[k][1])

        # Separa em uma lista as OPs que precisam sofre atualizacao
        # posicao 2 em K e a coluna acao devido a posicao dela no
        # resultado do 'cons_sql()'
        if k_op[k][2] == 3:
            list_ops_to_update.append(k_op[k])
            # print(f'\nAchei UP $$ {list_ops_to_update}\n')
        if k_op[k][2] == 2:
            list_ops_to_del.append(k_op[k])
            # print(f'\nAchei DEL !! {list_ops_to_del}\n')

    # print(f'\n^^^^^^^ {k_op}\n')
    df, dados = df_xls(list_op)
    df_inserted = pd.DataFrame(df)

    if not df_inserted.empty:
        # Separa apenas as OPS novas que foram para o BD para flag no excel
        ops_news_excel = df_inserted['OP']
        # Cria uma lista de controle de quais ops devem ser atualizadas
        # no Excel
        for op in ops_news_excel:
            ops_to_excel.append(op)
        if dados == 1:
            confirma_importacao(ops_to_excel)
        else:
            print('Erro 1001 - Insert no BD')

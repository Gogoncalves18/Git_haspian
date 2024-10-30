from conex_db import cons_sql
from df_dados import df_xls, df_nest
import pandas as pd
from atualiza_excel import confirma_importacao, confirma_importacao_nest
from conex_db import put_ofs, val_sql

valida_table, msg = val_sql()
if valida_table == 1 or valida_table == 2:
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
        # Executa a insercao dos arranjos
        df_arranjos, dados_arranjos = df_nest(list_op)

        # Separa apenas as OPS novas que foram para o BD para flag no excel
        ops_news_excel = df_inserted['OF']
        ops_news_excel_clean = set(ops_news_excel)
        ops_news_deactivate = set(df_arranjos['OF'])
        nestings = set(df_arranjos['ARRANJOS'])

        # Funcao para desativar OFs que serao replicadas para os nestings
        of_deactivated = put_ofs(df_arranjos, 'OfDeact', ops_news_deactivate, 0)
        # Funcao para inserir as chapas e associar os ParentID
        nest_inserted = put_ofs(df_arranjos, 'OfDeact', 0, nestings)

        # Cria uma lista de controle de quais ops devem ser atualizadas no Excel
        for op in ops_news_excel_clean:
            if op not in ops_to_excel:
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

            if k_op[k][1] not in list_op:
                list_op.append(k_op[k][1])
            # # Separa em uma lista as OPs que precisam sofre atualizacao
            # # posicao 2 em K e a coluna acao devido a posicao dela no
            # # resultado do 'cons_sql()'
            # elif k_op[k][2] == 3:
            #     if k_op[k][2] not in list_ops_to_update:
            #         list_ops_to_update.append(k_op[k])
            #         # print(f'\nAchei UP $$ {list_ops_to_update}\n')
            # elif k_op[k][2] == 2:
            #     if k_op[k][2] not in list_ops_to_del:
            #         list_ops_to_del.append(k_op[k])
            #         # print(f'\nAchei DEL !! {list_ops_to_del}\n')

        # Prepara os DF para inserir, atualizar ou deletar
        df, dados = df_xls(list_op)
        df_inserted = pd.DataFrame(df)
        df_arranjos, dados_arranjos = df_nest(list_op)

        if not df_inserted.empty or not df_arranjos.empty:
            ops_news_deactivate = set()
            # Separa apenas as OPS novas que foram para o BD para flag no excel
            ops_news_excel = df_inserted['OF']
            # Cria uma lista de controle de quais ops devem ser atualizadas
            # no Excel
            ops_news_excel_clean = set(ops_news_excel)

            # ###   tratar este dado que vem como float e deve ser str
            for i, raw in df_arranjos.iterrows():
                ops_news_deactivate.add(str(int(raw['OF'])))

            df_nest_to_import = df_arranjos[df_arranjos['ACAO'] == 1]
            nestings = set(df_nest_to_import['ARRANJOS'])

            # Funcao para desativar OFs que serao replicadas para os nestings
            if len(nestings) > 0:
                of_deactivated = put_ofs(df_arranjos, 'OfDeact', ops_news_deactivate, 0)
                # Funcao para inserir as chapas e associar os ParentID
                nest_inserted = put_ofs(df_arranjos, 'OfDeact', 0, nestings)

            for op in ops_news_excel_clean:
                if op not in ops_to_excel:
                    ops_to_excel.append(op)
            if dados == 1:
                confirma_importacao(ops_to_excel)
            else:
                print('Erro 1002 - Insert OPs individuais no BD')

            if dados_arranjos == 1:
                confirma_importacao_nest(nestings)
            else:
                print('Erro 1003 - Insert Arranjos no BD')
elif valida_table == 0:
    print(msg)

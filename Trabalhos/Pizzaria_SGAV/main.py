from infra.repository_bd.restauracao_bd import Restauracao_BD
from infra.repository_bd.restauracao_bd_cbo import Restauracao_BD_CBO
from modulos.bckup_banco import Movimentacao_Backups
from dotenv import load_dotenv
from os import getenv
import datetime
from datetime import timedelta
from infra.repository_bd.entregas_foody_rep import Entregas_FoodyD_Repository
from modulos.dados_foody_API import Entregas
from modulos.tratamento_dados_api import Tratamento_Dados_API

# Funcao para executar uma movimentacao de arquivos do bckup, estes
# arquvivos sao salvos pelo Colibri ERP em uma pasta e movimentados
# para outra pasta, extraidos, renomeados e restaurados
load_dotenv()
path_bck_pdv = getenv("local_origem_bcksql_pdv")
new_path_bck_pdv = getenv("local_destino_bcksql_pdv")
nome_fisco = getenv("nome_bck_fisco")
nome_venda_pdv = getenv("nome_bck_pdv_venda")
bak_sql_pdv = getenv("bak_sql_pdv")
path_bck_cbo = getenv("local_origem_bcksql_cbo")
new_path_bck_cbo = getenv("local_destino_bcksql_cbo")
nome_venda_cbo = getenv("nome_bck_cbo_venda")
bak_sql_cbo = getenv("bak_sql_cbo")

bck_pdv = Movimentacao_Backups(path_bck_pdv, new_path_bck_pdv, nome_fisco,
                               nome_venda_pdv, bak_sql_pdv)

bck_cbo = Movimentacao_Backups(path_bck_cbo, new_path_bck_cbo, nome_fisco,
                               nome_venda_cbo, bak_sql_cbo)

# Funcao para executar uma movimentacao de arquivos do bckup, estes
# arquvivos sao salvos pelo Colibri ERP em uma pasta e movimentados
# para outra pasta, extraidos, renomeados e restaurados
bck_pdv.mov_bckup()
restaurar_bd = Restauracao_BD()
restaurar_bd.restaurar_sql()

bck_cbo.mov_bckup()
restaurar_bd_cbo = Restauracao_BD_CBO()
restaurar_bd_cbo.restaurar_sql()

# Marcacao da data atual coletada pelo computador para servir de
# referencia para as funcoes de validacao de data para requisicao
# do json que preciso importar do pedido do Foody Delivery,
# formato da data '2024-06-21'
dt_fim = datetime.date.today()
# dt_BD referencia para ultima data lida no BD de entregas do Foody
dt_BD = ''
# Laco para executar requisicoes de 2 em 2 dias ate que o ultimo
# registro em BD seja igual a data atual dt_fim
entregas = Entregas_FoodyD_Repository()
while True:
    # Funcao que traz a ultima data do BD de entregas do foody,
    # se o BD estevir vazio, entao ele retorna uma lista vazia
    # Funcao do arquivo tratamento_json_sql.py
    next_data_sql = entregas.select_ultima_dt()
    # dt_in = '2024-06-21'
    # dt_fim = '2024-06-21'
    # Condicionais para tratar as situacoes que recebi da consulta
    if next_data_sql is None:
        dt_in = None
    else:
        dt_in = next_data_sql[0] + timedelta(days=1)
        dt_BD = next_data_sql[0] + timedelta(days=2)
    if dt_in is None:
        # Como o BD sempre devolve um DATETIME completo, isto e, com
        # data+hora+timezone
        # e necessario usar a funcao STRPTIME ao qual eu especifico qual
        # o formato de
        # dados que estou recebendo e em cima dele, apos identificado o
        # formato, posso
        # usar mais uma funcao, neste caso .DATE() para ele me retornar
        # apenas a data
        # data esta que e o ultimo registro do BD
        dt_BD = datetime.datetime.strptime('2025-04-25', '%Y-%m-%d').date()
        # Com uma data forcada '2024-06-21' que e o primeiro registro de
        # quando comecamos
        # usar o Foody Delivery e da data dt_BD de um dia para frente do atual
        # Chamo a funcao dentro de dados_foody_delivery.py
        corridas_por_dia = Entregas('2025-04-24', dt_BD)
        corridas = corridas_por_dia.entregas_foody_api()
        # print(corridas)
        list_pedidos = Tratamento_Dados_API().separacao_dados_para_sql(
            corridas)

        # if list_pedidos is True:
        #     break

        print('>>>>>>>>> Pedidos separados <<<<<<<')
        for pedido in list_pedidos:
            print("\n#################################################\n")
            print(pedido)
            entregas.insert_corridas(pedido[0],
                                     pedido[1],
                                     pedido[2],
                                     pedido[3],
                                     pedido[4],
                                     pedido[5],
                                     pedido[6],
                                     pedido[7],
                                     pedido[8],
                                     pedido[9],
                                     pedido[10],
                                     pedido[11],
                                     pedido[12],
                                     pedido[13],
                                     pedido[14],
                                     pedido[15],
                                     pedido[16],
                                     pedido[17],
                                     pedido[18],
                                     pedido[19],
                                     pedido[20],
                                     pedido[21],
                                     pedido[22],
                                     pedido[23]
                                     )
    elif dt_BD <= dt_fim:
        corridas_por_dia = Entregas(dt_in, dt_BD)
        corridas = corridas_por_dia.entregas_foody_api()
        list_pedidos = Tratamento_Dados_API().separacao_dados_para_sql(
            corridas)
        print('>>>>>>>>> Pedidos separados <<<<<<<')
        for pedido in list_pedidos:
            print("\n#################################################\n")
            print(pedido)
            entregas.insert_corridas(pedido[0],
                                     pedido[1],
                                     pedido[2],
                                     pedido[3],
                                     pedido[4],
                                     pedido[5],
                                     pedido[6],
                                     pedido[7],
                                     pedido[8],
                                     pedido[9],
                                     pedido[10],
                                     pedido[11],
                                     pedido[12],
                                     pedido[13],
                                     pedido[14],
                                     pedido[15],
                                     pedido[16],
                                     pedido[17],
                                     pedido[18],
                                     pedido[19],
                                     pedido[20],
                                     pedido[21],
                                     pedido[22],
                                     pedido[23]
                                     )
        # if list_pedidos is True:
        #     break
        # dt_BD = dt_BD + timedelta(days=1)
    else:
        break

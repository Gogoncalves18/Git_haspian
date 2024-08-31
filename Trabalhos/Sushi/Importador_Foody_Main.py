from dados_foody_delivery import entregas
from tratamento_json_sql import extracao_json
from tratamento_json_sql import verif_data_slq
import datetime
from datetime import timedelta
from mov_files_bckup import mov_bckup


def comunicacao_sql(res):
    # Pedidos dentro de uma list em LISTA_PEDIDOS
    # Status da request
    lista_pedidos = res.get('Dados_req').get('Dados_Recebido')
    status_code_req = res.get('Info_req').get('Status_Code')
    if status_code_req == 200:
        # Gero a extracao dos dados e comunicacao com SQL a partir
        # desta funcao que esta em TRATAMENTO_JSON_SQL
        extracao_json(lista_pedidos)
    else:
        print(status_code_req)
        err_req = True
        return err_req


# Funcao para executar uma movimentacao de arquivos do bckup, estes
# arquvivos sao salvos pelo Colibri ERP em uma pasta e movimentados
# para outra pasta, extraidos, renomeados e restaurados
mov_bckup()
# Marcacao da data atual coletada pelo computador para servir de
# referencia para as funcoes de validacao de data para requisicao
# do json que preciso importar do pedido do Foody Delivery,
# formato da data '2024-06-21'
dt_fim = datetime.date.today()
# dt_BD referencia para ultima data lida no BD de entregas do Foody
dt_BD = ''

# Laco para executar requisicoes de 2 em 2 dias ate que o ultimo
# registro em BD seja igual a data atual dt_fim
while True:
    # Funcao que traz a ultima data do BD de entregas do foody,
    # se o BD estevir vazio, entao ele retorna uma lista vazia
    # Funcao do arquivo tratamento_json_sql.py
    next_data_sql = verif_data_slq()
    # dt_in = '2024-06-21'
    # dt_fim = '2024-06-21'
    # Condicionais para tratar as situacoes que recebi da consulta
    if next_data_sql == []:
        dt_in = next_data_sql
    else:
        dt_in = next_data_sql
        dt_BD = next_data_sql + timedelta(days=1)
    if dt_in == []:
        # Como o BD sempre devolve um DATETIME completo, isto e, com
        # data+hora+timezone
        # e necessario usar a funcao STRPTIME ao qual eu especifico qual
        # o formato de
        # dados que estou recebendo e em cima dele, apos identificado o
        # formato, posso
        # usar mais uma funcao, neste caso .DATE() para ele me retornar
        # apenas a data
        # data esta que e o ultimo registro do BD
        dt_BD = datetime.datetime.strptime('2024-06-22', '%Y-%m-%d').date()
        # Com uma data forcada '2024-06-21' que e o primeiro registro de
        # quando comecamos
        # usar o Foody Delivery e da data dt_BD de um dia para frente do atual
        # Chamo a funcao dentro de dados_foody_delivery.py
        res = entregas('2024-06-21', dt_BD)
        # Funcao para listar os pedidos para extracao dos dados
        err_req = comunicacao_sql(res)
        # Se vier vazio, quebro o while
        if err_req is True:
            break
        # Incremento a data do banco para um novo laco ate dar vazio
        dt_BD = dt_BD + timedelta(days=1)
    elif dt_BD <= dt_fim:
        res = entregas(dt_in, dt_BD)
        err_req = comunicacao_sql(res)
        if err_req is True:
            break
        dt_BD = dt_BD + timedelta(days=1)
    else:
        break

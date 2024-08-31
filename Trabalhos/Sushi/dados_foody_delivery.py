import requests


def entregas(data_ini, data_fim):
    """Função para puxar JSON de uma API rest. A função devolve em formato
    de dict a INFO_REQ (contem status code e reason de resp) e DADOS_REQ
    quando ocorre tudo bem, vindo em formato json, dentro de DADOS_RECEBIDO.
    :param "data_ini" = recebe a data inicial para puxar os dados em
    formato YYYY-MM-DIA.
    :param "data_fim" = recebe a data final para puxar os dados em
    formato YYYY-MM-DIA.
    """

    # Recebo na funcao a data inicial e final da consulta no foody delivery,
    # o resto e o padrao que a ferramenta deles precisa, fixei pois a loja
    # so atende das 18h às 23h
    start_date = f"{data_ini}T18:00:00-03:00"
    end_date = f"{data_fim}T23:59:00-03:00"
    # Na biblioteca REQUEST eu posso gravar os parametros em uma variavel
    parametros = f'startDate={start_date}&endDate={end_date}'
    # URLPAG é a parte da minha requisicao que e padrao, seria meu ENDPOINT
    urlpag = 'https://app.foodydelivery.com/rest/1.2/orders/?'
    # NO CABECALHO eu passo as informacoes de autorizacao e especifico que
    # tipo de dado eu receberei assim como defino o padrao de caracter. Nem
    # toda API aceita receber estas infos no cabecalho
    cabecalho = {"Authorization": "8defdd57a07c419eab132fe5ddc97dec",
                 "Content-Type": "application/json;charset=UTF-8"}

    # A funcao GET() do request e a responsavel pela consulta e nela ha
    # um padrao para passar as variaveis. Apos instancio os dados
    response = requests.get(url=urlpag, headers=cabecalho, params=parametros)

    # Na instancia RESPONSE, receberei uma estrutura de dados dentro do dict
    # com 3 conjuntos de infos{status_code, reason, json}, os codigos dentro de
    # status_code de 200 a 299 e que deu boa, ha uma tabela universal para isto
    # Em resumo a funcao devolve toda esta estrutura {status_code, reason,
    # json}
    # ou devolve infos{status_code, reason}, sendo que eu estou reestruturando
    # a resposta para uma estrutura como esta
    # {"Info_req": {
    #               "Status_Code": response.status_code,
    #                    "Reason": response.reason},
    #                 "Dados_req": {"Dados_Recebido": response.json()}
    #               }
    if response.status_code >= 200 and response.status_code <= 299:
        dados_api = {"Info_req": {"Status_Code": response.status_code,
                     "Reason": response.reason},
                     "Dados_req": {"Dados_Recebido": response.json()}}
        return dados_api
    else:
        dados_api = {"Info_req": {"Status_Code": response.status_code,
                     "Reason": response.reason}}
        return dados_api

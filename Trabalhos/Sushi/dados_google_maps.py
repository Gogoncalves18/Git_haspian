import requests

# d = 'R. Konrad Adenauer', '911'
# lat_d = '-25.4354243'
# long_d = '-49.22411629999999'
# lat_o = '-25.42294'
# long_o = '-49.21656'


def geoloc_gmap(lat_d, long_d, lat_o, long_o):
    """
    Funcao para calcular tempo de rota em Min e KM.
    Dados de entrada:
    lat_d => latitude do destino
    long_d => longitudo do destino
    lat_o => latitude da origem
    long_o => longitude da origem

    Return da função:
    km => distancia em km na rota
    tempo => tempo em Min na rota
    """
    destino = f"destinations={lat_d}%2C{long_d}&"
    origem = f"origins={lat_o}%2C{long_o}&"
    parametros = f'{destino}{origem}'
    # Endpoint da api do developement google maps
    urlpag = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
    # esta api nao aceita enviar a key no cabecalho, estou enviando a toa
    req = f'{urlpag}{parametros}key=AIzaSyBjyfMdH2M6opd93rfSaF0EMQsv7rmq33c'

    cabecalho = {"Authorization": "AIzaSyBjyfMdH2M6opd93rfSaF0EMQsv7rmq33c",
                 "Content-Type": "application/json;charset=UTF-8"}

    # Instacio a resposta da api em response
    response = requests.get(url=req, headers=cabecalho, params=parametros)
    # print(req)
    # laco para tratar a resposta
    if response.status_code >= 200 and response.status_code <= 299:
        # Na instancia RESPONSE, receberei uma estrutura de dados dentro do
        # dict
        # com 3 conjuntos de infos{status_code, reason, json}, os codigos
        # dentro de
        # status_code de 200 a 299 e que deu boa, ha uma tabela universal
        # para isto
        # Em resumo a funcao devolve toda esta estrutura {status_code, reason,
        # json}
        # ou devolve infos{status_code, reason}, sendo que eu estou
        # reestruturando
        # a resposta para uma estrutura como esta
        # {"Info_req": {
        #               "Status_Code": response.status_code,
        #                    "Reason": response.reason},
        #                 "Dados_req": {"Dados_Recebido": response.json()}
        #               }
        dados_api = {"Info_req": {"Status_Code": response.status_code,
                     "Reason": response.reason},
                     "Dados_req": {"Dados_Recebido": response.json()}}
        # a API da google e uma serie de dados indentados dentro de listas,
        # por isto dos niveis de acesso dos valores
        km_rota = (((dados_api["Dados_req"]['Dados_Recebido']['rows'][0][
            'elements'][0]['distance']['value'])*1.60934)/1000)
        tempo_rota = (dados_api["Dados_req"]['Dados_Recebido']['rows'][0][
            'elements'][0]['duration']['value'])
        # formato para duas casas decimais a informacao
        km_rota = f'{km_rota:.2f}'
        # o tempo de rota vem se segundos, faco a conversao para minutos
        # e ainda aciono 1 minuto a mais
        tempo_rota = (tempo_rota//60)+1
        # Devolucao das duas informacoes para quem requisitou
        return km_rota, tempo_rota
    else:
        dados_api = {"Info_req": {"Status_Code": response.status_code,
                     "Reason": response.reason}}
        print('erro de requisicao')
        return km_rota, tempo_rota

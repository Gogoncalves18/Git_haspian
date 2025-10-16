import requests
from dotenv import load_dotenv
from os import getenv


class Entregas:
    '''
    Classse necessita receber:
    data_ini: data de início para extração de dados da API,
            no seguinte formato -> '2025-08-14'.
    data_fim: data de fim para extração de dados da API,
            no seguinte formato ->'2025-08-14' 
    '''
    load_dotenv()

    def __init__(self, data_ini, data_fim):
        self.__dt_inicial = data_ini
        self.__dt_final = data_fim
        self.__start_dt = f"{self.__dt_inicial}T18:00:00-03:00"
        self.__end_dt = f"{self.__dt_final}T23:59:00-03:00"

    def entregas_foody_api(self) -> dict:
        # Na biblioteca REQUEST eu posso gravar os parametros em uma variavel
        parametros = f'startDate={self.__start_dt}&endDate={self.__end_dt}'
        # URLPAG é a parte da minha requisicao que e padrao, seria meu ENDPOINT
        url_api = getenv('url_foody')
        # NO CABECALHO eu passo as informacoes de autorizacao e especifico que
        # tipo de dado eu receberei assim como defino o padrao de caracter. Nem
        # toda API aceita receber estas infos no cabecalho
        key_api = getenv('key_api_foody')
        cabecalho = {"Authorization": key_api,
                     "Content-Type": "application/json;charset=UTF-8"}

        # A funcao GET() do request e a responsavel pela consulta e nela ha
        # um padrao para passar as variaveis. Apos instancio os dados
        response = requests.get(url=url_api, headers=cabecalho,
                                params=parametros)

        # Na instancia RESPONSE, receberei uma estrutura de dados
        # dentro do dict
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
        if response.status_code >= 200 and response.status_code <= 299:
            dados_api = {"Info_req": {"Status_Code": response.status_code,
                         "Reason": response.reason},
                         "Dados_req": {"Dados_Recebido": response.json()}}
            return dados_api
        else:
            dados_api = {"Info_req": {"Status_Code": response.status_code,
                         "Reason": response.reason}}
            return dados_api


if __name__ == '__main__':
    ent = Entregas(data_ini='2025-08-14', data_fim='2025-08-14')
    res_ent = ent.entregas_foody_api()
    print(res_ent)

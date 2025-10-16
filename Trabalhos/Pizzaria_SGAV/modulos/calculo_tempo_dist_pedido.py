import requests
from dotenv import load_dotenv
from os import getenv


class Calcular_Tempo_Dist:

    def geoloc_gmap(self, lat_d, long_d, lat_o, long_o):
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
        load_dotenv()
        self.key_google_maps = getenv('key_google_maps')

        self.destino = f"destinations={lat_d}%2C{long_d}&"
        self.origem = f"origins={lat_o}%2C{long_o}&"
        self.parametros = f'{self.destino}{self.origem}'
        # Endpoint da api do developement google maps
        self.urlpag = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
        # esta api nao aceita enviar a key no cabecalho, estou enviando a toa
        self.req = f'{self.urlpag}{self.parametros}key={self.key_google_maps}'

        self.cabecalho = {"Authorization": self.key_google_maps,
                          "Content-Type": "application/json;charset=UTF-8"}

        # Instacio a resposta da api em response
        self.response = requests.get(url=self.req,
                                     headers=self.cabecalho,
                                     params=self.parametros)
        # print(req)
        # laco para tratar a resposta
        if self.response.status_code >= 200 and self.response.status_code <= 299:
            # Na instancia RESPONSE, receberei uma estrutura de dados dentro do
            # dict
            # com 3 conjuntos de infos{status_code, reason, json}, os codigos
            # dentro de
            # status_code de 200 a 299 e que deu boa, ha uma tabela universal
            # para isto
            # Em resumo a funcao devolve toda esta estrutura {status_code,
            # reason, json}
            # ou devolve infos{status_code, reason}, sendo que eu estou
            # reestruturando a resposta para uma estrutura como esta
            # {"Info_req": {
            #               "Status_Code": response.status_code,
            #                    "Reason": response.reason},
            #                 "Dados_req": {"Dados_Recebido": response.json()}
            #               }
            self.dados_api = {"Info_req": {"Status_Code": self.response.status_code,
                                           "Reason": self.response.reason},
                              "Dados_req": {"Dados_Recebido": self.response.json()}}
            # a API da google e uma serie de dados indentados dentro de listas,
            # por isto dos niveis de acesso dos valores
            self.km_rota = (((self.dados_api["Dados_req"]['Dados_Recebido']['rows'][0][
                'elements'][0]['distance']['value'])*1)/1000) # troquei milha por km 1.60934
            self.tempo_rota = (self.dados_api["Dados_req"]['Dados_Recebido']['rows'][0][
                'elements'][0]['duration']['value'])
            # formato para duas casas decimais a informacao
            self.km_rota = f'{self.km_rota:.2f}'
            # o tempo de rota vem se segundos, faco a conversao para minutos
            # e ainda aciono 1 minuto a mais
            self.tempo_rota = (self.tempo_rota//60)+1
            # Devolucao das duas informacoes para quem requisitou
            return self.km_rota, self.tempo_rota
        else:
            self.dados_api = {"Info_req": {"Status_Code": self.response.status_code,
                              "Reason": self.response.reason}}
            print('erro de requisicao')
            return self.km_rota, self.tempo_rota

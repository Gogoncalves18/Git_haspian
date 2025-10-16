import re
from modulos.calculo_tempo_dist_pedido import Calcular_Tempo_Dist
from datetime import datetime


class Tratamento_Dados_API:
    def __init__(self):
        self.__lista_pedidos = []

    @classmethod
    def __extracao_id(cls, inf):
        '''
        Mineracao de dados de um campo texto com varias informacoes.
        Objetivo e ler um codigo do pedido das plataformas ifood e
        jota ja que sao formados por 8 digitos de 0 a 9.
        '''
        try:
            # Instacio o que busco em uma variavel
            inf_id = (re.findall(r'[0-9]{8}', inf))[0]
        except IndexError:
            inf_id = ''
        # devolvo a informacao extraida se for encontrada
        return inf_id

    def separacao_dados_para_sql(self, dados: list) -> dict:
        # Pedidos dentro de uma list em LISTA_PEDIDOS
        # Status da request
        lista_pedidos = dados.get('Dados_req').get('Dados_Recebido')
        status_code_req = dados.get('Info_req').get('Status_Code')
        if status_code_req == 200:
            # Gero a extracao dos dados e comunicacao com SQL a partir
            # desta funcao que esta em TRATAMENTO_JSON_SQL
            return self.__extracao_json_api(lista_pedidos)
        else:
            print(status_code_req)
            err_req = True
            return err_req

    def __extracao_json_api(self, pedidos: dict):
        entrega_falsa = 1
        for i in pedidos:
            try:
                numentrega = int(i['id'])
            except ValueError:
                numentrega = 5000 + entrega_falsa
                entrega_falsa += 1
            uidcliente = i['uid']
            datapedido = datetime.strptime(
             i['date'], '%Y-%m-%dT%H:%M:%S-03:00').date()
            horapedido = datetime.strptime(
                i['date'], '%Y-%m-%dT%H:%M:%S-03:00').time()
            try:
                horapedpronto = datetime.strptime(
                    i['readyDate'], '%Y-%m-%dT%H:%M:%S-03:00').time()
            except KeyError:
                horapedpronto = datetime.strptime(
                    i['date'], '%Y-%m-%dT%H:%M:%S-03:00').time()
            try:
                horapedaceito = datetime.strptime(
                    i['acceptanceDate'], '%Y-%m-%dT%H:%M:%S-03:00').time()
            except KeyError:
                horapedaceito = datetime.strptime(
                    i['date'], '%Y-%m-%dT%H:%M:%S-03:00').time()
            try:
                horapedentregue = datetime.strptime(
                    i['deliveryDate'], '%Y-%m-%dT%H:%M:%S-03:00').time()
            except KeyError:
                horapedentregue = datetime.strptime(
                    i['date'], '%Y-%m-%dT%H:%M:%S-03:00').time()
            try:
                tempototentrega = str((
                    datetime.strptime(
                        i['deliveryDate'], '%Y-%m-%dT%H:%M:%S-03:00')
                ) - (
                    datetime.strptime(
                        i['readyDate'], '%Y-%m-%dT%H:%M:%S-03:00')
                ))
            except KeyError:
                tempototentrega = '00:20:00'
            try:
                txentrega = i['deliveryFee']
            except KeyError:
                txentrega = '0'
            try:
                txmotoboy = i['courierFee']
            except KeyError:
                txmotoboy = '0'
            try:
                motoboy = i['courier']['courierName']
            except KeyError:
                motoboy = 'nao identificado'
            try:
                nomecliente = i['customer']['customerName']
            except KeyError:
                nomecliente = ''
            try:
                telefone = i['customer']['customerPhone']
            except KeyError:
                telefone = ''
            rua = i['deliveryPoint']['street']
            numresid = i['deliveryPoint']['houseNumber']
            try:
                cidade = i['deliveryPoint']['city']
            except KeyError:
                cidade = 'none'
            coletalat = i['collectionPoint']['coordinates']['lat']
            coletalong = i['collectionPoint']['coordinates']['lng']
            lat = i['deliveryPoint']['coordinates']['lat']
            long = i['deliveryPoint']['coordinates']['lng']
            if "ID: " in i['notes']:
                obs = 'ifood'
            elif "*Jotaja" in i['notes']:
                obs = 'jotaja'
            else:
                obs = 'none'

            # Funcao para mineirar o campo de observacoes do pedido e
            # encontrar o id do pedido da do ifood ou jota ja
            iddelivery = Tratamento_Dados_API.__extracao_id(i['notes'])
            # funcao que aciona a api do google maps para calcular
            # distancia e tempo de uma rota ao qual entrego a geo
            # localizacao da origem e destino
            google_tempo_dist = Calcular_Tempo_Dist()
            dist, tempodist = google_tempo_dist.geoloc_gmap(lat, long,
                                                            coletalat,
                                                            coletalong)
            # print(">>> Dados de KM e Tempo extraídos da API do GoogleMaps")
            # print apenas para acompanhar o que o sistema esta inserindo
            # de pedido

            self.__lista_pedidos.append((
                numentrega,
                uidcliente,
                datapedido,
                horapedido,
                horapedpronto,
                horapedaceito,
                horapedentregue,
                tempototentrega,
                txentrega,
                txmotoboy,
                motoboy,
                nomecliente,
                telefone,
                rua,
                numresid,
                cidade,
                coletalat,
                coletalong,
                lat,
                long,
                obs,
                iddelivery,
                dist,
                tempodist
            ))
        print(">>> Dados extraídos da API do Foody")
        self.pedidos = self.__lista_pedidos
        return self.pedidos


if __name__ == '__main__':
    dados = {'Info_req': {'Status_Code': 200, 'Reason': 'OK'},
             'Dados_req': {'Dados_Recebido': [
                {'uid': '3ff9dfe6-e7b8-4fd9-992b-bb15745789e9',
                 'id': '1',
                 'status': 'closed',
                 'deliveryFee': 0.0,
                 'paymentMethod': 'money',
                 'notes': '',
                 'courierFee': 7.3,
                 'orderTotal': 67.25,
                 'orderDetails': '0x BUFALA ESPECIAL MD | R$ 38,50\n0x \
                                  MARGUERITA MD | R$ 28,75',
                 'despatchMode': 'manual',
                 'deliveryPoint': {'address': 'Rua Castro, 668, Água Verde,\
                                   Curitiba',
                                   'street': 'Rua Castro',
                                   'houseNumber': '668',
                                   'postalCode': '80620300', 'coordinates': {
                                       'lat': -25.45943, 'lng': -49.27954},
                                   'city': 'Curitiba', 'region': 'PR',
                                   'country': 'BRA', 'complement': ' | '},
                 'collectionPoint': {'id': '6266368411959296',
                                     'name': 'LAG GASTRONOMIA LTDA',
                                     'address': 'Rua Castro, 431 - Água Verde,'
                                     ' Curitiba - PR, Brasil',
                                     'coordinates': {'lat': -25.4576404,
                                                     'lng': -49.2783563},
                                     'city': '', 'region': '', 'country': '',
                                     'complement': ''},
                 'customer': {'customerPhone': '41996070012',
                              'customerName': 'Tereza Faria dos Santos',
                              'customerEmail': ''},
                 'courier': {'courierPhone': '+5541988110914',
                             'courierName': '30 - Wagner Barbosa ',
                             'courierType': 'internal'},
                 'date': '2025-08-16T18:04:05-03:00',
                 'despatchDate': '2025-08-16T18:19:32-03:00',
                 'acceptanceDate': '2025-08-16T18:19:48-03:00',
                 'collectedDate': '2025-08-16T18:20:42-03:00',
                 'deliveryDate': '2025-08-16T18:26:56-03:00',
                 'closedDate': '2025-08-16T18:27:28-03:00',
                 'creationDate': '2025-08-16T18:04:27-03:00',
                 'updateDate': '2025-08-16T18:27:28-03:00'
                 },
                {'uid': '4ba948fe-d518-460a-8774-9f7bdd9cc869',
                 'id': '2',
                 'status': 'closed',
                 'deliveryFee': 0.0,
                 'paymentMethod': 'card',
                 'notes': '*Jotaja_26061337*',
                 'courierFee': 7.3,
                 'orderTotal': 117.5,
                 'orderDetails': '0x FRANGO COM CATUPIRY MD | R$ 28,75\n0x \
                    NAPOLITANA MD | R$ 30,00\n0x MILHO MD | \
                    R$ 28,75\n0x PORTUGUESA MD | R$ 30,00',
                 'despatchMode': 'manual',
                 'deliveryPoint': {'address': 'Rua Mato Grosso, 491,\
                                    Água Verde, Curitiba',
                                   'street': 'Rua Mato Grosso',
                                   'houseNumber': '491',
                                   'postalCode': '80620070',
                                   'coordinates': {'lat': -25.46483,
                                                   'lng': -49.28548},
                                   'city': 'Curitiba',
                                   'region': 'PR', 'country': 'BRA',
                                   'complement': 'Ap 11 |\
                                    Igreja Catarina Laborê'},
                 'collectionPoint': {'id': '6266368411959296',
                                     'name': 'LAG GASTRONOMIA LTDA',
                                     'address': 'Rua Castro, 431 - Água Verde,\
                                          Curitiba - PR, Brasil',
                                     'coordinates': {'lat': -25.4576404,
                                                     'lng': -49.2783563},
                                     'city': '', 'region': '', 'country': '',
                                     'complement': ''},
                 'customer': {'customerPhone': '41984025278',
                              'customerName': 'Cintia Michalski',
                              'customerEmail': ''},
                 'courier': {'courierPhone': '+5541997891797',
                             'courierName': 'Francivaldo da Silva ',
                             'courierType': 'internal'},
                 'date': '2025-08-16T18:25:32-03:00',
                 'despatchDate': '2025-08-16T18:36:11-03:00',
                 'acceptanceDate': '2025-08-16T18:36:15-03:00',
                 'collectedDate': '2025-08-16T18:36:19-03:00',
                 'deliveryDate': '2025-08-16T18:47:36-03:00',
                 'closedDate': '2025-08-16T18:48:06-03:00',
                 'creationDate': '2025-08-16T18:26:27-03:00',
                 'updateDate': '2025-08-16T18:48:06-03:00'
                 }
                ]}
             }
    trat = Tratamento_Dados_API()
    trat.separacao_dados_para_sql(dados=dados)

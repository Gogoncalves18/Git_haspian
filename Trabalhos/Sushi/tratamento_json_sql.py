from datetime import datetime
from datetime import timedelta
import pyodbc
import re
from dados_google_maps import geoloc_gmap as gloc


# Dados de conexao para a biblioteca PYODBC, para conexao no sqlxpress
# instalado no mesmo equipamento. Neste caso há em uma instancia, 2 BD
# um para o erp Colibri e outro para as entregas do foody
driver = 'SQL Server Native Client 11.0'
server = 'YOGA9I\\ECSQLEXPRESS'
database = 'foodyd'
database2 = 'ncrcolibri'
username = 'None'
password = 'None'
tc = 'yes'

# Formato da str de conexao do PYODBC com os parametros para o BD
# que e utilizado pela biblioteca para executar as conexoes
str_conex = f"DRIVER={driver}; SERVER={server}; DATABASE={
                database}; UID={username}; PWD={
                password}; TRUSTED_CONNECTION={tc}"

str_conex2 = f"DRIVER={driver}; SERVER={server}; DATABASE={
                database2}; UID={username}; PWD={
                password}; TRUSTED_CONNECTION={tc}"


# Funcao para extrair os dados do json e preparar para insert SQL
def extracao_json(pedidos):
    '''
    Funcao para tratamento de dados de arquivo JSON para insercao
    no SQL. Esta funcao roda os dados do foody delivery recebido em
    uma lista e prepara as informacoes formatando e separando em:
    numentrega => numero inteiro para identificar entrega
    uidcliente => codigo hexadecimal do cliente
    datapedido => data curta apenas no formato 'YYYY-MM-DD'
    horapedido => derivado da data pedido com formato 'time()'
    horapedpronto => horario pedido pronto com formato 'time()'
    horapedaceito => horario aceito com formato 'time()'
    horapedentregue => horario entregue com formato 'time()'
    tempoentrega => tempo da corrida com formato 'time()'
    txentrega => taxa cobrada de entrega como str
    txmotoboy => valor a pagar para o motoboy como str
    motoboy => nome do motoboy como str
    nomecliente => nome do cliente ou telefone 0800 quando for ifood
    telefone => terá o numero do cliente quando for jota ja
    rua => nome da rua do cliente
    numres => numero da residencia em str por causa de letras
    cidade => nome da cidade do cliente
    coletalat => latitude da posicao de coleta
    coletalong => longitude da posicao de coleta
    lat => latitude da posicao de entrega
    long => longitude da posicao de coleta
    obs => observacoes do pedido, possui o ID do pedido usada na plataforma
    iddelivery =>
    dist => distancia percorrida da rota de entrega do sushi ao cliente
    tempodist => tempo de viagem estimada pelo google maps

    ---------------------------------------------------------

    Para os itens de hora quando eles falham, é capturado os tempos da
    horapedido.
    Quando o calculo de tempo de pedido falha, é usado 20min. Quando as taxas
    falham,
    é usada o valor 0. Quando o entregador falha, é usada nao identificado.
    Quando o
    cliente e telefone falham, é adicionado ''. Para cidade é adicionado none.

    '''
    lista_pedidos = []
    for i in pedidos:
        numentrega = i['id']
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
        iddelivery = extracao_id(i['notes'])
        # funcao que aciona a api do google maps para calcular
        # distancia e tempo de uma rota ao qual entrego a geo
        # localizacao da origem e destino
        dist, tempodist = gloc(lat, long, coletalat, coletalong)
        # print apenas para acompanhar o que o sistema esta inserindo
        # de pedido
        print(f'Data : {datapedido} <=> Numero Entrega : {numentrega}')
        # montado uma lista com todas as variaveis acima, esta lista
        # ajudara a acelerar o insert no sql atraves do pyodbc
        lista_pedidos.append((
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
            tempodist)
        )
    # Entrego a lista de insert de pedidos montada por dia para a
    # funcao que ficara encarregada de inserir os pedido no BD
    conexsql(lista_pedidos)


def conexsql(list_peds):
    '''
    Funcao para percorrer dados de pedidos que estao dentro de uma [].
    Ela procura 24 variaveis dentro dos dados que estao organizados na
    lista recebida.
    '''
    list_peds = list_peds
    # abro conexao e instacio
    conex = pyodbc.connect(str_conex)
    # aloco o cursor do pyodbc que executa os cmd
    cursor_sql = conex.cursor()
    # sintaxe do cmd que insere cada dado, cada ? e uma variavel inserida no bd
    cmd = "INSERT INTO entregas VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
    # necessario trabalhar com try em caso de insucesso no insert
    try:
        # sintaxe para inserir varios dados. Primeiro o cmd do sql e depois
        # uma lista contendo os dados em uma serie correta.
        # O executemany e para acelerar a insercao
        cursor_sql.executemany(cmd, list_peds)
        # confirmacao do inser no BD
        conex.commit()
    # Evocacao de msg para caso de erro
    except pyodbc.DatabaseError as avisos:
        # print da saida de erro
        print(avisos)
        # cancelamento dos dados enviado no bd
        conex.rollback()
    finally:
        # Necessario fechar a conexao instaciada
        conex.close()


# Funcao para ler ultima data no BD da Foody
def verif_data_slq():
    # Instancio a conexao com o BD em CONEX utilizando o cmd CONNECT e
    # a str de conexao
    conex = pyodbc.connect(str_conex)
    # Abro um funcao da biblioteca, CURSOR() e instancio ela para usar os cmds
    cursor_sql = conex.cursor()
    # Em variaveis monto os mesmos scripts do sql mantendo "" por fora e
    # simples por dentro
    cmd_cons = "select datapedido from dbo.entregas where idsushi = (select max(idsushi) from dbo.entregas)"
    # Recomendado abrir um try para controla insucessos no BD e tambem fechar
    # as conexoes abertas por cada cursor que executo
    try:
        # EXECUTE() e cmd do cursor que esta instanciado e nele eu devo passar
        # o script sql. O FETCHALL() neste caso e para atacar todas as linhas
        # da consulta
        inf = cursor_sql.execute(cmd_cons).fetchall()
        # Se o BD estiver sem registro, ele volta para mim uma []
        # senao voltara uma [(datetime.date(2024, 8, 27),)]
        if inf == []:
            # ULT_DATA gravo a info que retornou do BD
            ult_data = []
        else:
            # Uso o TIMEDELTA para descontar (dias, hora ou datas) de um campo
            # datetime em cima de um fatiamento que fiz dentro da [] gravada
            # em INF. Neste caso estou colocando um dia a mais que o registro
            # para devolver para o MAIN a info
            ult_data = (inf[0][0]) + timedelta(days=1)
        return ult_data
    # pyodbc.DatabaseError e onde recebo os erros das tratativas no SQL
    except pyodbc.DatabaseError as avisos:
        print(f'MENSAGEM DO SQL APOS INSUCESSO:\n\n{avisos}\n')
        # Sempre devemos aplicar um ROLLBACK() no PYODBC apos um insucesso
        conex.rollback()
    finally:
        # Por fim devo sempre fechar a conexao aberta pelo CURSOR()
        conex.close()


def extracao_id(inf):
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


def restaurar_sql(bak):
    '''
    Funcao para restauracao de backup de DB. A funcao deve receber
    o caminho completo e o nome do arquivo.bak
    '''
    # Abre conexao com o BD
    conex = pyodbc.connect(str_conex2)
    # Parametro executar obrigatoriamente commit no BD (consolidacao do dados)
    conex.autocommit = True
    # instacia o cursor do sql
    cursor_sql = conex.cursor()
    # estrutura do script do sql, primeiro uso o master para nao estar
    # concorrendo com o uso do BD enquanto tiver escrevendo o bckup.
    # depois aponto o nome do BD 'ncrcolibri' o local onde esta o bak e
    # a instrucao with replace para apenas substituir o bd ao inves de regravar
    cmd1 = f"""USE MASTER; RESTORE DATABASE ncrcolibri FROM DISK='{bak}' WITH REPLACE;"""
    try:
        # executa o cmd
        cursor_sql.execute(cmd1)
        # aqui um segredo, enquanto ocorre a restauracao do BD,
        # o cursor fica em aberto, se ele ler a linha abaixo que define
        # o fechamento da conexao, a restauracao do bak nao ocorre.
        # neste caso o sistema fica em loop validando se o cursor ainda
        # esta em aberto com o cursor_sql.nextset(), apos uma negativa
        # eu saiu do laco e entao encerro a conexao
        while cursor_sql.nextset():
            pass
        cursor_sql.close()
    except pyodbc.DatabaseError as avisos:
        print(f'PROBLEMA COM A MANIPULAÇÃO DO SQL\n:{avisos}')
        conex.rollback()
    finally:
        # linha de seguranca para o caso de dar tudo certo
        conex.close()

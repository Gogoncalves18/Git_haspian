import datetime
import os
import shutil
import zipfile
from tratamento_json_sql import restaurar_sql


def acao(raiz, file, new_root):
    """
    - Funcao para movimentar de local o arquivo.
    - Devo receber:
     # a raiz do local do arquivo
     # o nome do arquivo
     # o caminho que o arquivo deve ser salvo
    """
    # une caminho antigo e arquivo
    path_old = os.path.join(raiz, file)
    # une caminho novo e arquivo
    path_new = os.path.join(new_root, file)
    # Move o arquivo do caminho antigo para o novo
    shutil.move(path_old, path_new)
    # Chama a funcao para extrair o arquivo
    extracao_zip(new_root, path_new)
    return print('ARQUIVO MOVIDO')


def extracao_zip(new_root, path_new):
    """
    Funcao para extracao dos arquivos de um zip.
    - Necessario receber:
     # new_root = caminho relativo onde o arquivo deve ser salvo
     # path_new = caminho relativo+arquivo do zip
    """
    # acionamento do pacote zip instanciando em zip
    with zipfile.ZipFile(path_new, 'r') as zip:
        # extracao de tudo que ha nele
        zip.extractall(new_root)
        # funcao que me devolve uma lista que contem o que ha
        # de arquivo dentro do zip, usada para pegar o nome
        # do arquivo
        nome_arq = zip.namelist()[0]
    # validacao se ha o nome dentro do arquivo
    if 'ncrcolibri' in nome_arq:
        # instacio o caminho e arquivo onde salvei o conteudo
        # que é um bak
        new_file = os.path.join(new_root, nome_arq)
        # caminho onde sempre irei resgatar o bak atual
        baksql = 'C:\\Program Files\\Microsoft SQL Server\\MSSQL15.ECSQLEXPRESS\\MSSQL\\Backup\\ncrcolibri.bak'
        # movimentacao do arquivo para o local de bak do sql
        # importante, tive que usar o copy2 que era capaz de gravar na
        # pasta do sql e manter os direitos de uso dos usuarios do sistema
        # que no caso seria o usuario do bd e instancia
        shutil.copy2(new_file, baksql)
        # valido se o arquivo existe la, se sim deleto
        if os.path.exists(new_file):
            os.remove(new_file)
        # Aciona a funcao que conversa com o BD e executa o script SQL
        restaurar_sql(baksql)
        print('Arquivo BAK criado')


def mov_bckup():
    """
    Funcao para movimentacao do bckup do sql em zip de um local
    do dropbox para outro local. Apos extracao do arquivo, renomeacao
    e movimentacao para a pasta de bckup do sql
    """
    # assumo data atual para buscar os bckup do dia, os anteriores
    # sao deixados para traz
    dt_now = str(datetime.date.today())
    # Procuro dois arquivos importante, o bck das vendas que tem o nome
    # ncrcolibri e o do fiscal que tera sempre o nome FiscalGateway, ambos
    # zipados e em ambos eu concateno com a data atual para desconsiderar
    # os demais
    name_file = f'ncrcolibri-{dt_now.replace('-', '')}'
    fisco = f'FiscalGateway-{dt_now.replace('-', '')}'
    # local de nivel mais alto onde os arquivos sao colocados
    root = 'C:\\Users\\gogon\\Dropbox\\GOG\\SH 1\\Dani Gerente\\Fluxo de Caixa\\'
    # local que eu quero movimentar os arquivos, este local ninguem tem acesso
    new_root = 'C:\\Users\\gogon\\Dropbox\\GOG\\SH 1\\BCKUP_Automotizado_COLIBRI\\'
    # Uso walk para varrer os arquivos e pastas
    for raiz, subfolders, files in os.walk(root):
        for file in files:
            # validacao, se encontrar, envia para outra funcao
            if name_file in file:
                # Funcao para movimentar
                acao(raiz, file, new_root)
            elif fisco in file:
                # Funcao para movimentar
                acao(raiz, file, new_root)
            else:
                pass
    # retorna um valor para quem chama a funcao
    return 'AÇÃO DE MANIPULAÇÃO DE ARQUIVO REALIZADA'


# imprime na tela a execucao deste script
print(mov_bckup())

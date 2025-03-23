import datetime
import os
import shutil
import zipfile


class Movimentacao_Backups:

    def __init__(self, path_default: str, new_path: str, nome_fisco: str,
                 nome_venda: str, bak_sql_pdv: str):
        self.path_default = path_default
        self.new_path = new_path
        self.nome_fisco = nome_fisco
        self.nome_venda = nome_venda
        self.bak_sql = bak_sql_pdv

    def mov_bckup(self) -> None:
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
        name_file = f'{self.nome_venda}-{dt_now.replace('-', '')}'
        fisco = f'{self.nome_fisco}-{dt_now.replace('-', '')}'
        root = self.path_default
        # local que eu quero movimentar os arquivos, este local ninguem tem
        # acesso
        new_root = self.new_path
        # Uso walk para varrer os arquivos e pastas
        for raiz, subfolders, files in os.walk(root):
            for file in files:
                # validacao, se encontrar, envia para outra funcao
                if name_file in file:
                    # Funcao para movimentar
                    self.__acao(raiz, file, new_root)
                elif fisco in file:
                    # Funcao para movimentar
                    self.__acao(raiz, file, new_root)
                else:
                    pass

    def __acao(self, raiz, file, new_root):
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
        print(f'## BCKUP >>> {file} <<< MOVIDO')

        # Chama a funcao para extrair o arquivo
        self.__extracao_zip(new_root, path_new)

    def __extracao_zip(self, new_root, path_new):
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
        if self.nome_venda in nome_arq:
            # instacio o caminho e arquivo onde salvei o conteudo
            # que é um bak
            new_file = os.path.join(new_root, nome_arq)
            # caminho onde sempre irei resgatar o bak atual
            baksql = self.bak_sql
            # movimentacao do arquivo para o local de bak do sql
            # importante, tive que usar o copy2 que era capaz de gravar na
            # pasta do sql e manter os direitos de uso dos usuarios do sistema
            # que no caso seria o usuario do bd e instancia
            shutil.copy2(new_file, baksql)
            # valido se o arquivo existe la, se sim deleto
            if os.path.exists(new_file):
                os.remove(new_file)
            # Aciona a funcao que conversa com o BD e executa o script SQL
            print(f'## BAK >>> {nome_arq} <<< NA POSICAO PARA RESTAURACAO')
            # restaurar_sql(baksql)

import os  # Usado para tratar caminhos de pastas e arquivos
import shutil
import re  # Usado para minerar os nomes das pastas
import csv  # Usado para ler os dados gerado por excel


# Caminho CSV que servira como base para comparar o codigo de mercado
# com o codigo interno do ERP, formato deve ser:
# codigo_interno;codigo_mercado com a primeira linha para nome de coluna
source_file = 'C:\\Users\\gogon\\Documents\\Inga\\cam\\inga.csv'

lista_cod = []  # Dados do csv serao guardado nesta variavel
# Leitura do csv e apendi dos dados em uma lista
with open(source_file, newline='') as file_obj:
    spamreader = csv.reader(file_obj, delimiter=';')
    for nl, line in enumerate(spamreader):
        if nl > 0:  # Pula a primeira linha que tem cabecalho
            lista_cod.append(str(line[0]))  # Posicao codigo_interno
            lista_cod.append(str(line[1]))  # posicao codigo_mercado

# Expressao regular para minerar os nomes de pastas
expressao = re.compile(r'_|-|\(|\)|,')  # Simbolos utilizados no cliente
expressao_2 = re.compile(r'\.')  # Segundo nível de mineracao para tratar
# dados que estão com ponto
# expressao_3 = re.compile


# FUNCOES DE CONTROLE PARA TRATAMENTO DE NOMES EM PASTAS
def tratamento_nomes_pasta(caminho, arq_cnc, ext_arq_cnc):
    '''Esta funcao deve receber um caminho raiz e uma pasta de
    ultimo nível antes do arquivo a ser manipulado. Estas infos
    estao sendo encaminhadas para funcao em formato de list'''

    # A lista recebida com raiz e última pasta do caminho do arquivo
    # é tratada para entregar a variavel word apenas a ultima pasta
    # que sera manipulada
    word = str(caminho[-1])
    print(f"ORIGEM ==== > {caminho}")  # Validacao do caminho em list
    # Acionamento da expressao para minerar o nome do arquivo no primeiro
    # nivel, inserimos espacos em todos caracteres "_-()," encontrados
    # no nome do arquivo, posterior, este nome é dividido pelos espaços
    # para formar uma lista de possiveis codigos
    print(f'ARQUIVO => {arq_cnc} - EXT => {ext_arq_cnc}')
    saneamento_word_n1 = expressao.sub(' ', word).split(' ')
    # Validação da lista de codigos que foi extraida no nivel I
    print(f'SANEAMENTO DE: {saneamento_word_n1}')
    # Trecho é cada possivel codigo dentro da lista
    for trecho in saneamento_word_n1:
        # Quando encontrado pontos dentro de uma possível codigo
        # faco mais uma mineracao nivel II para segmentar mais
        if '.' in trecho:
            saneamento_word_n2 = expressao_2.sub(' ', trecho).split(' ')
            # print(f'ENCONTREI ESTA LISTA DE PONTOS => {saneamento_word_n2}')
            # Variavel que servira como base para aplicar os futuros
            # testes, ela se reescreve a cada testagem
            cod_ficticio = saneamento_word_n2
        else:
            # print(f'ACHEI PALAVRA ==> {trecho}')
            cod_ficticio = trecho
        # Apos fazer a grava dos possíveis codigos, rodamos a verificacao
        # se estes possiveis codigos existem na lista de codigos em CSV
        for ni, item in enumerate(lista_cod):
            # Como o csv possui apenas duas colunas sendo a segunda posicao
            # sempre para o codigo_mercado, sempre que o item for par, isto e,
            # estiver na primeira posicao da lista, ele nao interessa para
            # encontrar o codigo de mercado
            if (ni % 2) != 0:
                # Nova validacao para saber se estou recebendo um 'trecho' ao
                # qual já foi devidamente separado ou se estou recebendo uma
                # lista para ser tratada de forma diferente
                if type(cod_ficticio) is str and len(cod_ficticio) > 2:
                    if str(cod_ficticio) == str(item):
                        # Valida se pasta e o item encontrado
                        # print(f'OLHA O QUE ACHEI::::> Pedaço da pasta\
                        # com {cod_ficticio} e encontrei com CoD_Merc {item}')
                        # Mostra a posicao do item no cvs ou lista, se usar o
                        # notepad++ fica facil de conferir
                        print(f'ELE está: COD_M POS \
{((lista_cod.index(item))+3)/2} com COD_i \
{lista_cod[lista_cod.index(item)-1]}')
                        # Funcao para tratar o item = CODIGO_MERCADO
                        # lista_cod com CODIGO_INTERNO
                        mov_pastas_arqs(item,
                                        lista_cod[
                                            lista_cod.index(item)-1],
                                        arq_cnc, ext_arq_cnc)
                    # Nova validacao para remover um caracter final
                    # para procurar novo match com o csv
                    elif str(cod_ficticio[:-1]) == str(item):
                        # print(f'OLHA O QUE ACHEI::::> Pedaço da pasta \
                        # com {cod_ficticio} e encontrei com CoD_Merc {item}')
                        print(f'ELE está: COD_M POS \
{((lista_cod.index(item))+3)/2} com COD_i \
{lista_cod[lista_cod.index(item)-1]}')
                        mov_pastas_arqs(item,
                                        lista_cod[lista_cod.index(item)-1],
                                        arq_cnc, ext_arq_cnc)
                # Aqui executo nova analise apenas para codigo que
                # formaram uma lista
                elif type(cod_ficticio) is list:
                    # Todas as possiveis partes de um pseudo codigo é
                    # reavaliada para analisar um novo match com o csv
                    for frag_cod_list in cod_ficticio:
                        if str(frag_cod_list) == str(item):
                            print(f'ELE está: COD_M POS \
{((lista_cod.index(item))+3)/2} com COD_i \
{lista_cod[lista_cod.index(item)-1]}')
                            mov_pastas_arqs(item,
                                            lista_cod[
                                                lista_cod.index(item)-1],
                                            arq_cnc, ext_arq_cnc)


def mov_pastas_arqs(cod_mercado, cod_interno, arq_cnc, ext_arq_cnc):
    '''Funcao para copiar e renomear novas pastas para outro
    ambiente, aqui recebemos os dois códigos, mercado e interno'''
    print(f'ESTE CÓDIGO MERCADO TEM NA LISTA: {cod_mercado} \
Referenciado com {cod_interno}')
    # Desempacotando em maquinas e pastas das maquinas para preservarmos
    # a mesma nomenclatura
    maqs, pasta_maq_origem = os.path.split(last_nivel_pasta[0])
    new_path = new_ponto_zero + pasta_maq_origem + separador + cod_interno
    # Validacoes se existe pastas e subpastas na estrutura antes
    # de tentar criar os novos niveis
    if os.path.exists(new_path) is False:
        if os.path.exists(new_ponto_zero + separador +
                          pasta_maq_origem) is False:
            os.mkdir(new_ponto_zero + separador + pasta_maq_origem)
            os.mkdir(new_path)
        else:
            os.mkdir(new_path)
    if cod_mercado in arq_cnc:
        path_new_file = os.path.join(new_path, arq)
        arq_txt = new_path + separador + cod_interno + ".txt"
        shutil.copy(old_path_arq, path_new_file)
        qtd_L = int(arq_cnc.count('L'))
        if qtd_L == 0:
            arq_txt = new_path + separador + cod_interno + ".txt"
            shutil.copy(old_path_arq, arq_txt)
        elif qtd_L == 1:
            pos_L = int(arq_cnc.find('L') + 1)
            arq_txt = new_path + separador + cod_interno + "_L" + arq_cnc[pos_L] + ".txt"
            shutil.copy(old_path_arq, arq_txt)
    else:
        path_new_file = os.path.join(new_path, arq)
        arq_txt = new_path + separador + cod_interno + ".txt"
        shutil.copy(old_path_arq, path_new_file)
        shutil.copy(old_path_arq, arq_txt)
        print(arq_cnc)


# Variaveis de ambiente para leitura no caminho original e caminho novo
ponto_zero = 'C:\\Users\\gogon\\Documents\\Inga\\teste tornos\\gl250'
separador = '\\'
new_ponto_zero = 'C:\\Users\\gogon\\Documents\\Inga\\NOVOS tornos' \
                + separador


# Programa Principal
# Leitura de pastas e subpastas até chegar na base do arquivo
for raiz, subpastas, arqs in os.walk(ponto_zero+separador):
    for arq in arqs:
        print()
        # print(arq)  # Verificar qual arquivo está chegando
        old_name_arq = arq  # Nome antigo do arquivo para controle
        # Caminho antigo completo com o nome do arquivo antigo p/ controle
        old_path_arq = raiz+separador+old_name_arq
        # Quebra em arquivo e extensao
        old_name_arq_sem_ext, ext_arq = os.path.splitext(arq)

        # Tupla contendo o caminho em 0 e 1 o ultimo nivel de pasta na
        # estrutura que o OS.path caminha, variavel utilizada para manipular
        # a ultima pasta antes do arquivo final
        last_nivel_pasta = os.path.split(raiz)

        # Acionamento da função para tratar os nomes das pastas, dando
        # o caminho até a ultima pasta que contem um arquivo
        tratamento_nomes_pasta(last_nivel_pasta, old_name_arq_sem_ext, ext_arq)

        

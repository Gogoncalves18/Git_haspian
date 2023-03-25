from Modulos_Uteis import cores #Para trabalhar cores na saída do terminal


def arq_existe(nome):
    """Função para validar se há algum arquivo no local que será processado informações. A função devolve False se o arquivo não foi encontrado ou True se existe arquivo.
    :param "nome" = recebe o nome sem caminho ou como caminho para validar sua existência em disco.
    """
    try:
        cad = open(nome, 'rt') #Comando open do python. 'r' está pegando o arquivo como leitura e o 't' determina para o python que é um arquivo texto.
        cad.close() #sempre fechar depois que abre o programa para não conrromper.
    except FileNotFoundError: #Ser ele der erro ao não encontrar o programa, eu retorno com False
        return False
    else:
        return True
    

def criar_arq(nome):
    """Função para criar um arquivo.
    :param 'nome' = informar para função o nome do arquivo
    """
    try:
        cad = open(nome, 'wt+') #Comando 'w' abre o arquivo como escrita, o 't' informa ao python que é um texto e '+' define ao python que é para gerar o arquivo em disco.
        cad.close() #Fechar o arquivo para não corromper
    except:
        print(f'\n{cores.texto("Erro ao criar o arquivo", 1)}') #Gero mensagem apenas para saber que o programa falhou aqui


def inserir_p(arq, nome, idade):
    """Função para escrever dentro de um arquivo texto informações específicas que entram por parâmetro da função.
    : param 'arq' = deve receber o nome completo do arquivo que ele precisa acessar para escrever.
    : param 'nome' = deve receber o nome da pessoa que quero inserir no arquivo
    : param 'idade' = deve receber a idade da pessoa.
    """
    try:
        cad = open(arq, 'at') #Comando 'a' gera um apendi no arquivo e o 't' passa para o python que é texto.
    except:
        print(f'\n{cores.texto("Erro ao abrir para escrever", 1)}') #Mensagem para erros neste ponto
    else:
        try:
            cad.write(f'{nome};{idade}\n') #comando 'write' para escrever dentro do arquivo como um print formatado. O '\n' serve para pular de linha, pois fica gravado dentro do arquivo.
        except: 
            print(f'\n{cores.texto("Erro ao inserir infos no CAD", 1)}') #Mensagem para erros neste ponto
        else:
            print(f'{cores.texto(f"{nome} inserido com sucesso.", 4)}')
        finally:
            cad.close() #A principal função do 'finally' é encerrar a atividade final da função quando tudo executar, neste caso o close() é usado para fechar o arquivo que foi aberto.


def ver_cad(arq):
    """Função para acessar e ler os dados de um arquivo e mostrar em formato tabular através de um print.
    : param 'arq' = deve receber o nome completo do arquivo que deve ser acessado. 
    """
    try:
        cad = open(arq, 'rt') #Abre o arquivo como leitura e texto e joga dentro de CAD
    except:
        print(f'\n{cores.texto("Erro ao abrir arquivo para ler.", 1)}') #Mensagem para erro na operação anterior
    else: 
        #print(cad.read()) #Comando para ler o arquivo do jeito que ele está.
        print(f'{"NOME":<15}{"":^20}{"IDADE":>5}')
        print('')
        for l in cad: #Leio o texto por linha nesta laço FOR
            info_l = l.split(';') #Como o texto vem com "nome;idade", este comando quebra ele em uma lista dividindo em dois dados através do ';'.
            info_l[1] = info_l[1].replace("\n","") #Como há um "\n" ao fim de cada linha, este comando influencia no print posterior, contudo removemos o "\n" através do replace, o replace não funciona em um print formatado
            print(f'{info_l[0]:<15} {"-"*10:^15} {info_l[1]:>5} anos') #Aqui apenas estou tabulando a informação que sairá em um menu
    finally:
        cad.close() #Fecho o arquivo    

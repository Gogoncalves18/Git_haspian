def cadastrar_livro(id):
    """ Função para agregar ao acervo os livros cadasrados pelo user.
        Este processo possui validação de resposta sobre a efetivação
        do cadastro e dá oportunidade para o user verificar se os
        dados estão corretos antes de prosseguir com o cadastro.
    """

    global id_global
    id_global = id
    cad_livro = {}
    nome_l = input('\nNome do Livro: ')
    autor_l = input('Autor do Livro: ')
    editora = input('Editora do Livro: ')
    while True:
        inserir_cad = str(input('\nConfirma os dados acima? [S]\
 ou [N]').upper())
        try:
            if inserir_cad == 'S':
                cad_livro['id'] = id_global + 1
                cad_livro['nome_l'] = nome_l
                cad_livro['autor_l'] = autor_l
                cad_livro['editora'] = editora
                lista_livro.append(cad_livro.copy())
                break
            elif inserir_cad == 'N':
                print(cad_livro)
                break
            else:
                print('\nDigite apenas [S] ou [N]\n')
                continue
        except ValueError:
            print('\nNão é aceito números')
    id_global += 1


def consultar_livro():
    """
    Função para fazer 3 tipos de consultas no acervo. Ler todos livros
    Consultar por ID e Consultar por autor.
    """
    # Tela de opções
    print(f'{"\n\033[0;33;40mDeseja consultar por:\033[m":^86}')
    print(f'{"[1] - Consultar todos livros\n[2] - Consultar por ID\
         \n[3] - Consultar por Autor\n[4] - Retornar ao menu\n"}')
    while True:  # validação de entrada
        try:
            cons_user = int(input('OPÇÃO DESEJADA: '))
        except ValueError:
            print('\033[1;30;41m\nDigite uma opção válida!\033[m')
            continue
        # Validação se entrar com alguma opção fora das possibilidades
        if cons_user <= 0 or cons_user >= 5:
            print('\033[1;30;41m\nDigite uma opção válida!\033[m')
            continue
        elif cons_user == 1:
            # Saída no terminal para apresentar todos os livros
            # Com formatação de cores em volta
            print('\033[0;32;40mResultado de sua pesquisa:\033[m')
            for i in lista_livro:  # leitura do acervo em items
                print('\033[0;32;40m*\033[m' * 48)
                for k, v in i.items():  # Leitura dos dados do Dict
                    print(f'\033[0;32;40m*\033[m {k:<20} =>\
 {v:<20} \033[0;32;40m*\033[m')
                print('\033[0;32;40m*\033[m' * 48,)
            break
        elif cons_user == 2:  # Consulta por ID com apoio de outra funcao
            while True:  # Validação de entrada
                try:
                    cons_pers_user = int(input('\nPesquisar por ID: '))
                    print('\033[0;32;40mResultado de sua pesquisa:\033[m')
                    # Entrega de dados para ser tratada em outra função
                    proc_dados('id', cons_pers_user)
                    break
                except ValueError:
                    print('\n\033[1;30;41mEntre apenas com número\
 inteiro!\033[m')
            break
        elif cons_user == 3:  # Procura pelo auto
            cons_pers_user = input('\nPesquisar por Autor: ')
            print('\033[0;32;40mResultado de sua pesquisa:\033[m')
            # Entrega de dados para ser tratada por outra função
            proc_dados('autor_l', cons_pers_user)
            break
        elif cons_user == 4:  # Encerramento
            break


# Função de apoio do consultar_livro()
def proc_dados(chave, valor):
    """ Função para facilitar as pesquisas dentro do código
        CONSULTAR_LIVRO() para evitar de repetir códigos semelhantes
    """
    for i in lista_livro:
        # Varrer os itens do acervo e lê Chave e valor dentro do dict
        if i[chave] == valor:
            print('\033[0;32;40m*\033[m' * 48)
            for k, v in i.items():
                print(f'\033[0;32;40m*\033[m {k:<20} =>\
 {v:<20} \033[0;32;40m*\033[m')
            print('\033[0;32;40m*\033[m' * 48)


# Função para remover livro do acervo
def remover_livro():
    while True:  # Looping para validação de entrada
        try:
            # Validação de numero inteiro para carregar o ID
            id_user_remov = int(input('\nID de livro para deletar: '))
        except ValueError:
            print('\n\033[1;30;41mDigite um ID existente!\033[m')
        else:
            cont = 0  # Contador para controle de posição na Lista Acervo
            # leitura de cada elemento do acervo que está em dict
            for i in lista_livro:
                # Validação do ID de cada dict para ver se está batendo
                # com o ID a ser removido
                if i['id'] == id_user_remov:
                    del lista_livro[cont]  # Exclusão do item encontrado
                else:
                    cont += 1  # Adição de valor para leitura da próxima
                    # posição
        break


# PROGRAMA PRINCIPAL PARA QUESTAO 4
# Tela de boas vindas com nome
print('\033[1;7;41m\n Bem vindo a SUATECA do Gustavo de Oliveira\
 Gonçalves \033[m')

# Variaveis de cadastro
id_global = int(0)  # ID de controle inicial
lista_livro = []  # Lista que será alimentada, conterá o ACERVO

# Menu do main
while True:  # Looping para rodar o menu principal das escolhas
    # 3 prints abaixo com formatação de cor e centralização de str
    print(f'\033[0;33;40m\n{"-" * 25} {"MENU PRINCIPAL":^30}{"-" * 25}\033[m')
    print(f'{"Escolha a opção desejada:":^86}')
    print(f'{"[1] - Cadastrar Livro\n[2] - Consultar Livro\
         \n[3] - Remover Livro\n[4] - Encerrar Programa\n"}')
    try:  # Validação de etrar numerica
        menu_user = int(input('OPÇÃO DESEJADA: '))
    except ValueError:
        print('\033[1;30;41m\nDigite uma opção válida!\033[m')
        continue
    if menu_user <= 0 or menu_user >= 5:
        # Validacao de entrada com opção de 1 a 4 apenas
        print('\033[1;30;41m\nDigite uma opção válida!\033[m')
        continue
    elif menu_user == 1:
        # Chamada de função para cadastrar, ao qual é passada em qual
        # ID temos salva
        cadastrar_livro(id_global)
        continue
    elif menu_user == 2:
        # Chamada de função para consultas
        consultar_livro()
        continue
    elif menu_user == 3:
        # Chamada de função para remoção de livros do acervo
        remover_livro()
        continue
    elif menu_user == 4:
        # Finalização de programa
        break

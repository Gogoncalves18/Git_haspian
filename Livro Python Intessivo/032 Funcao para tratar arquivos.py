source_file = '/home/gog/Documentos/Python/Git_haspian/Livro Python Intessivo/pi.txt' #defino o local de tratamento
with open(source_file) as file_object:
#With aponta que vou usar a função de abrir um arquivo, o python decide quando vai fecha-lo
#'as' irá mascarar a função com o nome 'file_object' que será um objeto
    conteudo = file_object.read() #descarrego tudo em uma variável
    print(conteudo)

    #Ler o documento linha a linha
    n_line = 0
    for line in file_object:
        n_line += 1
        print(f'L{n_line} - {line}')

    #Metodo do Object que converte cada linha em um STR dentro de uma lista. Lines é uma lista!
    lines = file_object.readlines()
    for line in lines:
        n_line += 1
        print(f'L{n_line} {line}')

    #Metodo para montar várias linhas de um texto em uma linha só:
    pi_string = ''
    lines = file_object.readlines()
    for line in lines:
        pi_string += line.strip() #Este strip corta os espaço de pulo de linha
    print(pi_string[:500])
    print(len(pi_string))
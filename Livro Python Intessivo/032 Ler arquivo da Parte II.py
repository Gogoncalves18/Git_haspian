source_file = '/home/gog/Documentos/Python/Git_haspian/Livro Python Intessivo/texto_teste.txt'
with open(source_file, 'r+') as file_object:
    conteudo = ''
    for line in file_object:
        conteudo += line
    print(conteudo)
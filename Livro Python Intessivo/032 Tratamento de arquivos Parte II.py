source_file = '/home/gog/Documentos/Python/Git_haspian/Livro Python Intessivo/texto_teste.txt'
with open (source_file, 'wt+') as file_object:
    file_object.write('Eu estou gostando de programa. Mas talvez: \nLevarei mais tempo para aprender')
    file_object.write('Mas aos poucos estou conseguindo me virar.\nAgora é focar, para tentar fazer meu melhor')
    file_object.close()
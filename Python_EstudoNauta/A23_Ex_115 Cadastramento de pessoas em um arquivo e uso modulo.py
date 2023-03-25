'''Programa para cadastrar nome de pessoas e idade em um arquivo.
Ele deve ter 3 opções, cadastrar, ver cadastro e sair. Devesse
usar modulos e pacotes'''


from Modulos_Uteis import cores, file_creater #Funções apemas para criar arquivo e printar com cores


#Programa principal
arq = "cadastro_p.txt" #Nome do arquivo que gravarei a informações de nome e idade das pessoas
#arq = "perfil.txt"
if file_creater.arq_existe(arq) is False:  #Valido se há o arquivo no local que roda o programa
    file_creater.criar_arq(arq) #Se não há arquvivo eu o crio
while True:
    cores.titulo('Cadastro de Pessoas Físicas', 2) #Título 
    print(f'\n{cores.texto("[ 1 ] ",2)}{cores.texto("Cadastrar Nome e Idade", 3)}')
    print(f'{cores.texto("[ 2 ] ", 2)}{cores.texto("Ver Cadastro de Pessoas", 3)}')
    print(f'{cores.texto("[ 3 ] ", 2)}{cores.texto("Encerrar Programa", 3)}')
    try:
        print()
        opcao = int(input(cores.texto("Digite uma opção: ", 3))) #Peço para escolher uma das 3 opções acima
    except ValueError:
        print(cores.texto("Você precisa digitar uma opção válida!", 1)) #Validação de dado, se digitar alguma coisa diferente 
    else: 
        if opcao == 1: #Abro o cadastro de pessoa
            f'{cores.titulo("Opção 1 - Cadastrar Nome e Idade", 3)}' 
            nome = str(input('\nDigite nome: '))
            idade = int(input('Digite a idade: '))
            file_creater.inserir_p(arq, nome, idade) #Comando (Uma função que criei na pasta de Módulos_Uteis" para gravar dentro do arquivo TXT que já existe as informações que peguei no input
        elif opcao == 2: #Ver o cadastro
            f'{cores.titulo("Opção 2 - Cadastro", 3)}'
            file_creater.ver_cad(arq) #Apenas uso uma função criada na pasta Módulos_Uteis
        elif opcao == 3: #Encerro o programa
            f'{cores.titulo("Opção 3 - Programa encerrado", 2)}'
            break
        elif opcao not in (1,3) or opcao is not int: #Apresento mensagem diferente se digitar alguma opção que não seja algo entre 1 e 3
            f'{cores.titulo("Digite uma opção válida", 1)}'
        
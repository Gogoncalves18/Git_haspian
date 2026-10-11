class Paciente:
    '''Classe para criar os objetos que representarão os pacientes'''
    def __init__(self, num_pac, cor, next_num=None):
        self.num_pac = num_pac
        self.cor = cor
        self.next_num = next_num

    def __repr__(self):
        if self.next_num is not None:
            prox = self.next_num.num_pac
        else:
            prox = None

        return f'[Pac: {self.num_pac} Cor: {self.cor} Prox_Pac: {prox}]'


class Lst_chamada:
    '''Classe para controlar que entra e sai da lista e suas sequencia'''
    # Controlador do numero da ficha por tipo de paciente
    num_ficha_A = 201
    num_ficha_V = 1

    def __init__(self):
        '''serve apenas para eu guardar o meu Head'''
        self.head = None

    def inserirComPrioridade(self, cor):
        '''Nesta funcao recebo apenas um tipo de prioridade de paciente'''
        if cor == 'A':
            # Quando não tenho head em minha lista, o primeiro entra aqui
            if self.head is None:
                pac = Paciente(self.num_ficha_A, cor)
                self.num_ficha_A += 1
                self.head = pac
                return
            # Quando o head possui um prioridade menor que o paciente
            # que acabou de ser avaliado, entra aqui
            elif self.head.cor == 'V':
                pac = Paciente(self.num_ficha_A, cor)
                self.num_ficha_A += 1
                changed_head = self.head
                self.head = pac
                self.head.next_num = changed_head
                return
            else:
                ficha_0 = self.head
                pac = Paciente(self.num_ficha_A, cor)
                # Quando possuo head e nem um outro elemento a frente
                if ficha_0.next_num is None:
                    # Condiciona para trocar o verde pelo amarelo no head
                    if ficha_0.cor == 'V':
                        pac.next_num = ficha_0
                        self.head = pac
                    else:
                        ficha_0.next_num = pac
                # Quando já possuo dois ou mais elementos na fila,
                # entra neste laco
                else:
                    atual_fila = ficha_0
                    ant_fila = None
                    # Varre a linked list para conhecer os elementos
                    # até encontrar o tail da list
                    while atual_fila.next_num is not None:
                        # Desconsidero o elemento se for amarelo
                        if atual_fila.cor == 'A':
                            ant_fila = atual_fila
                            atual_fila = atual_fila.next_num
                        # Valido se o elemento lido da fila é o meu head
                        # para saber se tenho elemento anterior a ele
                        elif atual_fila == self.head:
                            ant_fila = atual_fila
                            atual_fila = atual_fila.next_num
                        # Valido se estou entre uma ficha Amarela e um Verde
                        # para decidir onde inserir o proximo elemento Amarelo
                        elif atual_fila.cor == 'V' and ant_fila.cor == 'A'\
                                and pac.cor == 'A':
                            ant_fila.next_num = pac
                            pac.next_num = atual_fila
                            break
                        # Se nao encontrar nenhum dos criterios acima,
                        # neste laco apenas avanca para o proximo elemento
                        else:
                            ant_fila = atual_fila
                            atual_fila = atual_fila.next_num
                    # Se chegarmos no Tail da Linked List,
                    # mudamos o atual tail para o novo tail e
                    # linkamos os penultimo elemento ao novo Tail
                    pac.next_num = atual_fila
                    ant_fila.next_num = pac
                # Incremento da ficha de controle
                self.num_ficha_A += 1
                return

    def inserirSemPrioridade(self, cor):
        '''Funcao para controlar os paciente sem prioridade'''
        # Quando não tenho head em minha lista, o primeiro entra aqui
        if self.head is None:
            pac = Paciente(self.num_ficha_V, cor)
            self.num_ficha_V += 1
            self.head = pac
            return
        else:
            ficha_0 = self.head
            pac = Paciente(self.num_ficha_V, cor)
            # Quando possuo head e nem um outro elemento a frente
            if ficha_0.next_num is None:
                ficha_0.next_num = pac
                self.num_ficha_V += 1
                return
            else:
                atual_fila = ficha_0
                ant_fila = None
                # Varre a linked list para conhecer os elementos
                # até encontrar o tail da list
                while atual_fila.next_num is not None:
                    # Se o elemento da fila lido for Amarelo parto p/ proximo
                    if atual_fila.cor == 'A':
                        ant_fila = atual_fila
                        atual_fila = atual_fila.next_num
                    # Valido se o elemento lido da fila é o meu head
                    # para saber se tenho elemento anterior a ele
                    elif atual_fila == self.head:
                        ant_fila = atual_fila
                        atual_fila = atual_fila.next_num
                    # Valido se estou entre uma ficha Amarela e um Verde
                    # para decidir onde inserir o proximo elemento Amarelo
                    elif atual_fila.cor == 'V' and ant_fila.cor == 'A'\
                            and pac.cor == 'A':
                        ant_fila.next_num = pac
                        pac.next_num = atual_fila
                    # Se nao encontrar nenhum dos criterios acima,
                    # neste laco apenas avanca para o proximo elemento
                    else:
                        ant_fila = atual_fila
                        atual_fila = atual_fila.next_num

                # Se chegarmos no Tail da Linked List,
                # mudamos o atual tail para o novo tail e
                # linkamos os penultimo elemento ao novo Tail
                atual_fila.next_num = pac
                self.num_ficha_V += 1
                return

    def imprimirListaEspera(self):
        '''Funcao para imprimir a lista de pacientes em espera'''
        # Padrao visual: fundo BRANCO e letra CINZA
        print('\n\033[0;41;47m LISTA DE ESPERA: \033[m\n')
        if self.head is not None:
            pac = self.head
            if pac.next_num is None:
                print(pac)
            while pac.next_num is not None:
                print(pac, end=" -> ")
                pac = pac.next_num
            return
        else:
            print('\nHEAD está vazio\n')
            return

    def atenderPaciente(self):
        # Padrao visual: fundo BRANCO e letra VERMELHA
        print(f'\n\033[0;31;47m Paciente da Ficha: {self.head.num_pac} \033[m\n')
        print('\033[0;31;47m Se apresente na sala do médico! \033[m\n')
        # Define o futuro HEAD da Linked List
        next_head_queue = self.head.next_num
        # Quebro a referencia do atual head que foi chamado
        self.head.next_num = None
        # Forco o python a deletar o obj que nao me interessa mais
        del self.head
        # Aponta o novo HEAD para Linked List
        self.head = next_head_queue


class Aval_paciente:

    def inserir():
        while True:
            # Padrao visual: fundo PRETO e letra AMARELA
            print('\n\033[0;33;40m# Aponte o grau de gravidade do paciente #\033[m\n')
            # Padrao visual: fundo PRETO e letra VERDE
            print('\033[0;32;40m[V] - Cartão Verde (CASO NORMAL)\033[m\n'
                  '\033[0;32;40m[A] - Cartão Amarelo (CASO URGENTE)\033[m\n')
            try:
                menu = str(input('\nDigite uma opção do menu acima: '))[0].upper()
                if menu == 'V':
                    lista_pac.inserirSemPrioridade(menu)
                    return
                elif menu == 'A':
                    lista_pac.inserirComPrioridade(menu)
                    return
                elif menu not in ['V', 'A']:
                    # Padrao visual: fundo PRETO e letra VERMELHA
                    print('\033[0;31;40m ====> Você deve digitar apenas uma das opções <==== \033[m')
            except ValueError:
                # Padrao visual: fundo PRETO e letra VERMELHA
                print('\033[0;31;40m ====> Você deve digitar apenas uma das opções <==== \033[m')


# Programa principal
# Uso da classe para controlar a linked List
lista_pac = Lst_chamada()
# Laco para controle do menu
while True:
    # Padrao visual: fundo PRETO e letra AMARELA
    print('\n\033[0;33;40m======= Selecione a opção desejada ===========\033[m\n')
    # Padrao visual: fundo PRETO e letra VERDE
    print('\033[0;32;40m[1] - Adicionar paciente a fila\033[m\n'
          '\033[0;32;40m[2] - Mostrar pacientes na fila\033[m\n'
          '\033[0;32;40m[3] - Chamar paciente\033[m\n'
          '\033[0;32;40m[4] - Sair\033[m\n')
    # Controle de digitacao errada por parte do user
    try:
        menu = int(input('\nDigite uma opção do menu acima: '))
        if menu == 1:
            Aval_paciente.inserir()
        elif menu == 2:
            lista_pac.imprimirListaEspera()
        elif menu == 3:
            lista_pac.atenderPaciente()
        elif menu == 4:
            break
        elif menu not in [1, 2, 3, 4]:
            # Padrao visual: fundo PRETO e letra VERMELHA
            print('\033[0;31;40m ====> Você deve digitar apenas uma das opções <==== \033[m')
    except ValueError:
        # Padrao visual: fundo PRETO e letra VERMELHA
        print('\033[0;31;40m ====> Você deve digitar apenas uma das opções <==== \033[m')

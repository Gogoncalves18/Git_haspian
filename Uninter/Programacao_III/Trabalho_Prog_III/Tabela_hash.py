def func_hash(uf: str, tam_a: int) -> int:
    '''Funcao para calcular uma posicao em um array
    para inserir o head de uma linked list.
    - uf:: string de duas posicoes representando o estado.
    - tam_a:: inteiro com o tamanho do array para calcular hash.

    Return:: define a posicao da chave (UF) no array dos heads.
    '''
    pos = None
    # Uso da funcao para transformar alphanumerico em valores da
    # tabela ASCII
    l1 = ord(uf[0])
    l2 = ord(uf[1])
    # O resto da divisão pelo tamanho do array irá determinar a
    # posicao do head
    pos = (l1+l2) % tam_a
    return pos


class Uf:
    '''Classe para criar os objetos que representarão os estados.
        - uf:: string de duas posicoes representando o estado.
        - nome_uf:: str com o nome completo do estado.
        - next_uf:: ponteiro que receberá um obj do UF para localizar
          o proximo obj.
    '''

    def __init__(self, uf: str, nome_uf: str, next_uf=None):
        self.uf = uf
        self.nome_uf = nome_uf
        self.next_uf = next_uf

    def __repr__(self):
        '''F(x) para representar o obj em linguagem natural'''
        if self.next_uf is not None:
            prox_uf = self.next_uf.uf
        else:
            prox_uf = None

        return f'[UF: {self.uf} - Nome: {self.nome_uf} - Prox_UF: {prox_uf}]'


class Lst_UF:
    '''Classe para controlar o que entra e sai
      da linked list dentro de uma posicao de array'''

    def __init__(self):
        '''serve apenas para eu guardar o meu Head'''
        self.head = None

    def inserir_UF_tab_hash(self, pos_na_tabH: int, uf: object):
        '''F(x) para controlar quem será o head em cada
            posição dentro do array da tabela hash.
        '''
        # Regra especial para o estado DF
        if uf.uf == 'DF':
            vetor_dados[7] = uf
            return
        # Primeiro head da posicao
        if vetor_dados[pos_na_tabH] is None:
            vetor_dados[pos_na_tabH] = uf
        # Fazer a troca do head dentro de uma posicao ocupada
        else:
            uf_before = vetor_dados[pos_na_tabH]
            uf.next_uf = uf_before
            vetor_dados[pos_na_tabH] = uf

    def listar_linked_list(self, head_pos: object):
        '''Funcao para imprimir a lista de UF encadeada pelo head'''

        self.head = head_pos
        # Percorre a linked list a partir do head
        if self.head is not None:
            uf_linked = self.head
            if uf_linked.next_uf is None:
                print(uf_linked.uf)
            while uf_linked.next_uf is not None:
                print(uf_linked.uf, end=" -> ")
                uf_linked = uf_linked.next_uf
            print(uf_linked.uf)
            return
        else:
            print('\nNão possuo head para encadear a lista!\n')
            return

    def listar_tab_hash(self):
        '''
        F(x) para listar tudo que temos nas posições do array
        que guarda os heads da linked list. O primeiro item dentro
        de cada posição é o head, os demais itens na mesma posição
        são itens que pertencem a uma linked list guardada em alguma
        posição na memória.
        '''
        # Controlador para definir o valor da posição no array de heads
        pos_i = 0
        # Padrao visual: fundo BRANCO e letra CINZA
        print('\n\033[0;41;47m LISTA DE UF POR POSIÇÃO NO ARRAY: \033[m\n')
        # Controlador para definir o quando eu preciso mudar de linha
        # no print de posiões no array do head.
        mudar_linha = 0
        # Laco para definir entre mudar de posição no array ou
        # chamar o proximo elemento do linked list.
        for i in vetor_dados:
            # Define se alinho o print na mesma linha ou na debaixo
            if mudar_linha == 1:
                print(f'\n{pos_i}: ', end='')
            else:
                print(f'{pos_i}: ', end='')
            # Define se apenas vou imprimir o elemento da posicao
            # do array de heads OU vou entrar nos lacos que
            # buscam os elementos do linked list
            if i.next_uf is None:
                print(f'{i.uf}', end=' ')
                print(f' -> {None}')
                pos_i += 1
                mudar_linha = 1
            else:
                self.listar_linked_list(i)
                pos_i += 1
                mudar_linha = 1


# MAIN PROGRAM
tam_a = 10
# Vetor vazio para ser populado com os HEADS da minha TABELA HASH
vetor_dados = [None, None, None, None, None, None, None, None, None, None]
# Dict dos estados por UF e nome completo escrito em hardcode
dict_UF = {
    "AC": "Acre",
    "AP": "Amapá",
    "AM": "Amazonas",
    "PA": "Pará",
    "RO": "Rondônia",
    "RR": "Roraima",
    "TO": "Tocantins",
    "AL": "Alagoas",
    "BA": "Bahia",
    "CE": "Ceará",
    "MA": "Maranhão",
    "PB": "Paraíba",
    "PE": "Pernambuco",
    "PI": "Piauí",
    "RN": "Rio Grande do Norte",
    "SE": "Sergipe",
    "ES": "Espírito Santo",
    "MG": "Minas Gerais",
    "RJ": "Rio de Janeiro",
    "SP": "São Paulo",
    "PR": "Paraná",
    "SC": "Santa Catarina",
    "RS": "Rio Grande do Sul",
    "DF": "Distrito Federal",
    "GO": "Goiás",
    "MT": "Mato Grosso",
    "MS": "Mato Grosso do Sul"
}

tab_hash = Lst_UF()

print('\n Tabela HASH antes das inserções dos estado:\n')
# Controlador para posicao do vetor
index = 0
# Impressao do array para provar que esta vazio
for i in vetor_dados:
    print(f'{index}: {i}')
    index += 1

# Percorre o dict de UF's e calcula a hash de posicao para cada um deles
for i in dict_UF.items():
    # Resultado da f(x) para calcular o HASH de posicao
    pos_uf = func_hash(i[0], tam_a=tam_a)
    # Construção do OBJ do estado com atr de UF, nome e proximo UF encadeado
    obj_uf = Uf(uf=str(i[0]), nome_uf=str(i[1]))
    # Chamada da f(x) para decidir se há um novo head no array
    # de heads ou se havera um novo elem encadeado
    tab_hash.inserir_UF_tab_hash(pos_uf, obj_uf)

# Imprime a lista completa da tabela hash sem UF ficticio
tab_hash.listar_tab_hash()
print()

# Imprime a lista completa da tabela hash COM UF ficticio
pos_uf = func_hash('GG', tam_a=tam_a)
uf_ficticio = Uf(uf='GG', nome_uf='Gustavo Gonçalves')
tab_hash.inserir_UF_tab_hash(pos_uf, uf_ficticio)
print('\n\033[0;31;47m PRÓXIMA LISTA SERÁ COM ESTADO FICTÍCIO: \033[m\n')
tab_hash.listar_tab_hash()
print()

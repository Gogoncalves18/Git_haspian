class Select:
    def by_id(self, id) -> any:
        print('\n<<< Selecionando elementos do DBO:')
        print(f'Elemento ID >>> {id}')


class Insert:
    def inserting(self) -> None:
        print('\n>>>> Inserindo elementos no DBO')


class Repositorio:
    # Na composicao nao carregamos no construtor a obj, somente
    # e diretamente no atr
    def __init__(self) -> None:
        self.__select = Select()  # Composicao de dependencia
        self.__insert = Insert()

    def select_by_id(self, id: int) -> any:
        self.__select.by_id(id)


repo = Repositorio()
repo.select_by_id(2)

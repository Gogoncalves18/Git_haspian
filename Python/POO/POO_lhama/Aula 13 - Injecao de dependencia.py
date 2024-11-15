
# responsavel pelo objeto de conexao de BD
class ConectorBD:
    def __init__(self) -> None:
        self.conex = None

    def conectar_bd(self) -> None:
        self.conex = True


# Classe para as ações do BD, o CRUD
class RepositorioBD:
    '''Classe criada para executar as acoes do BD'''
    def __init__(self, conexao: ConectorBD) -> None:
        self.__conexed = conexao

    def busca_dados(self) -> list:
        if self.__conexed.conex:
            return [1, 2, 3, 4]
        else:
            return None


# Aqui devemos desenvolver as regras dos que vamos fazer com os dados
# solicitados
class RegraNegocio:
    def __init__(self, repo: RepositorioBD) -> None:
        self.__repo = repo

    def calc_soma_dos_resultados(self) -> None:
        dados = self.__repo.busca_dados()
        if not dados:
            print('\nDados não encontrados')
        else:
            resp = 0
            for dado in dados:
                resp += dado
            print(f'\nA soma dos resultados foi {resp}')


# Instacia o BD
conn = ConectorBD()
# Abre a conexao com o BD
conn.conectar_bd()

# Passa a conexao para um objeto que podera fazer as consultas
repo = RepositorioBD(conn)
# Instancio as regras de negocio
regra = RegraNegocio(repo)

# Acionamento das regras que desencadeia todo do processo de conexao ao BD
regra.calc_soma_dos_resultados()

class Celular:
    def __init__(self, mod_cel: str) -> None:
        self.mod_cel = mod_cel

    def enviar_mensagem(self, msg: str) -> None:
        print(f'Enviando mensagem {msg}')

    def abri_emails(self) -> None:
        print("Abrindo Emails...")

    def abri_youtube(self) -> None:
        print("Abrindo Youtube...")


# Veja que estou entrando com o obj da classe dentro do atr do construtor
# diferente da aula 10 que eu instanciava dentro do metodo.
class Pessoa:
    def __init__(self, cel: Celular) -> None:
        # Sempre que temos uma injeção de dependência, precisamos colocar
        # atr como privado, para evitar acessos como o código REF001
        self.__cel = cel

    def pedir_pizza(self) -> None:
        print('\nPegando o celular...')
        print('Definindo o sabor ...')
        self.__cel.enviar_mensagem('quero uma pizza bacon e milho')

    def estudar(self) -> None:
        print('\nSentando no computador')
        self.__cel.abri_youtube()
        print('Anotando o material do vídeo')


samsung = Celular('Android')
iphone = Celular('Apple')

'''Esta é uma injeção de dependência, ao definir que gustavo e diego
são pessoas, eu obrigatóriamente preciso passar o objeto que foi 
instaciado pela classe Celular'''
gustavo = Pessoa(samsung)
diego = Pessoa(iphone)

print('<<<<<<<<<<>>>>>>>>>')
gustavo.estudar()
print('<<<<<<<<<<>>>>>>>>>')
diego.pedir_pizza


# diego.cel.abri_emails()  # REF001

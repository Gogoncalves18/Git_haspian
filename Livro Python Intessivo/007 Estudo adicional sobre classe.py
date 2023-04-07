#https://www.hashtagtreinamentos.com/classes-no-python?gclid=Cj0KCQjwz6ShBhCMARIsAH9A0qWMUJEgtE8M6lx6_kOOR5LZvH7WjqbFNutjw8RLI7C9xV0L-G8A_YAaAgffEALw_wcB
#metodos são sempre o verbo, isto é, o que fará
#atributos são as caracteristicas que ele possui


class Control_Virt:
    """Classe para dar funções de controle remoto para alguma tarefa ou automação"""
    def __init__(self, device):
        self.device = device #recebe o nome do dispositivo
        self.status = 0 #variavel para saber se já está ligado

    def botao_on_off(self):
        if self.status == 0:
            self.status = 1
            return f'\nO aparelho {self.device} está DESLIGADO, ligando AGORA...'
        else:
            self.status = 0
            return f'\nO aparelho {self.device} está LIGADO, desligando AGORA...'       

    def validar_sinal(self): #validando se ao clicar em algum comando, verifico se a TV está ligada
        if self.status == 0:
            return f'Ligue a TV primeiro' 
        else:
            return ''                       

    def botao_vol_subir(self):
        print(f'\nAumentando Volume do {self.device} para +')

    def botao_vol_descer(self):
        print(f'\nDiminuindo Volume do {self.device} para -')

    def botao_canal_subir(self):
        print(f'\nTrocando canal do {self.device} para +')

    def botao_canal_descer(self):
        print(f'\nTrocando canal do {self.device} para -')


#Programa Principal

tv = Control_Virt('tv')
htv = Control_Virt('htv')
while True:
    """Comandos para manipulação de controle:
        param: S - Sai do programa
        param: 8 - troca canal para cima
        param: 2 - troca canal para baixo
        param: 6 - aumenta volume
        param: 4 - diminui volume
        param: 5 - liga e desliga aparelho        
        """
    tecla = str(input('=> Recebendo CMD:'))
    if tecla == 's':
        break
    elif tecla in '8':
        if tv.validar_sinal() in '':
            tv.botao_canal_subir()
        else:
            print(tv.validar_sinal())
    elif tecla in '2':
        if tv.validar_sinal() in '':
            tv.botao_canal_descer()
        else:
            print(tv.validar_sinal())
    elif tecla in '6':
        if tv.validar_sinal() in '':
            tv.botao_vol_subir()
        else:
            print(tv.validar_sinal())
    elif tecla in '4':
        if tv.validar_sinal() in '':
            tv.botao_vol_descer()
        else:
            print(tv.validar_sinal())
    elif tecla in '5':
        print(tv.botao_on_off())
        print(htv.botao_on_off())

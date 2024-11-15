class MinhaClasse:
    def __init__(self, txt) -> None:  # Metodo construtor
        print('REF_A - Passei pelo construtor')
        self.atr1 = 'atr 1 - adicao manual'
        self.atr2 = txt
        self.atr3 = [1, 2, 4]

    def metod_1(self):
        print('REF_B - Minha acao 1')

    def metod_2(self, num_ext):
        '''Recebe um numero externo e soma ao atr3 da pos1'''
        print(f'REF004 - Meu resultado = {self.atr3[1] + num_ext}')


# Objeto    # Classe instaciada em um objeto
'''Vemos que primeira linha do programa é do main, esta abaixo, após ela chama
minha classe para passar pelo contrutor para depois exeutar o resto do
programa.'''
turma_1 = MinhaClasse("Entra via funcao do atr 2")

# Local onde o metodo se encontra na memoria e no programa
print(f'\nREF001 - {turma_1.metod_1}')

# Local onde a classe se encontra na memoria
print(f'REF002 - {MinhaClasse("Entra via funcao do atr 2")}')

# Local onde o objeto se encontra na memoria
print(f'REF003 - {turma_1}\n')

turma_1.metod_1()

# REF004
turma_1.metod_2(10)

# # ---------------------------------------------------------------------------------------------------------------------
# # Tema 2 part1
# # Definindo o decorator
# def meu_decorator(funcao_injetada):
#     def wrapper():  # Padrao de nome dado quando modifico uma funcao do código
#         print("A função será executada agora.")  # Trecho modificado com meu decorator
#         funcao_injetada()  # Trecho para chamo a funcao injetada
#         print("A função foi executada.")  # Trecho modificado com meu decorator

#     return wrapper  # Preciso devolver o resultado da nova funcao para o código


# # Aplicando o decorator usando o símbolo @
# # Ao aplicar o decorator, ele automaticamente jogará minha funcao original para
# # dentro da funcao decorada chama "meu_decorator()", para ela fazer isto, basta eu
# # chamar o nome dela com @
# @meu_decorator  # Trecho que injeta uma funcao dentro da outra
# def minha_funcao():
#     print("Esta é a função original.")


# # Chamando a função decorada
# minha_funcao()
# # ---------------------------------------------------------------------------------------------------------------------

#

# ---------------------------------------------------------------------------------------------------------------------
# Tema 2 part2
import time


# Definindo o decorator para medir o tempo de execução
def medir_tempo(funcao_injetada):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        # Entro com "*args, **kwargs" dentro da funcao quando estou passando
        # parametros pela funcao
        resultado = funcao_injetada(*args, **kwargs)
        fim = time.time()
        print(f"A função '{funcao_injetada.__name__}' demorou {fim - inicio:.6f} segundos para ser executada.")
        return resultado

    return wrapper


# Aplicando o decorator usando o símbolo @
# Esta aplicacao estamos medindo o tempo que levamos para executar cada
# trecho do codigo abaixo
@medir_tempo
def exemplo_funcao(tempo_espera):
    time.sleep(tempo_espera)
    print("A função foi executada.")


@medir_tempo
def exemplo_funcao2(tempo_espera):
    time.sleep(tempo_espera)
    print("A função foi executada.")


# Chamando a função decorada
exemplo_funcao(2)
exemplo_funcao2(4)

# # ---------------------------------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------------------------------
# # Tema 2 part3
# # Definindo o decorator de classe
# class Carro:
#     def __init__(self, classe_decorada):
#         self.classe_decorada = classe_decorada

#     def __call__(self, *args, **kwargs):
#         # Instancia a classe original
#         instancia_classe = self.classe_decorada(*args, **kwargs)
#         # Adiciona o atributo extra
#         instancia_classe.num_rodas = 4
#         return instancia_classe


# # Aplicando o decorator de classe usando o símbolo @
# @Carro
# class Automovel:
#     def __init__(self, modelo):
#         self.modelo = modelo


# # Criando uma instância da classe decorada
# new_auto = Automovel('Gol')

# # Chamando o método da classe e exibindo o atributo extra
# print(new_auto.modelo)
# print(new_auto.num_rodas)
# # ---------------------------------------------------------------------------------------------------------------------

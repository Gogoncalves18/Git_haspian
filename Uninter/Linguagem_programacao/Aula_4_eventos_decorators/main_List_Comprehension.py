import time


def medir_tempo(function):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = function(*args, **kwargs)
        fim = time.time()
        duracao = fim - inicio
        print(f"a {function.__name__} levou {duracao} segundos")
        return resultado

    return wrapper


@medir_tempo
def retorna_lista_par_sem_comprehension(max_value):
    lista_pares = []
    for num in range(max_value):
        if num % 2 == 0:
            lista_pares.append(num)
    return lista_pares


@medir_tempo
def retorna_lista_par_com_comprehension(max_value):
    lista_pares = [num for num in range(max_value) if num % 2 == 0]
    return lista_pares


retorna_lista_par_sem_comprehension(100000000)
retorna_lista_par_com_comprehension(100000000)

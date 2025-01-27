import numpy
from dotenv import load_dotenv
from os import getenv
import os

def combinar(iterable, r):
    char = tuple(iterable)
    n = len(char)

    if r > n:
        return

    index = numpy.arange(r)

    # returns the first sequence
    yield tuple(char[i] for i in index)

    while True:

        for i in reversed(range(r)):
            if index[i] != i + n - r:
                break
        else:
            return

        index[i] += 1

        for j in range(i + 1, r):
            index[j] = index[j - 1] + 1

        yield tuple(char[i] for i in index)

def conf_existe(arq):
    try:
        with open(arq) as arq_res:
            if arq_res:
                return True
    except FileNotFoundError:
        return False


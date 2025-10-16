import re


def valid(dado):
    info = None
    # Procura valor com XX.XX (numeros)
    info = re.findall(r'[0-9]{1,2}\.[0-9]{1,2}', dado)
    if info:
        return 'NUM'
    # Procura valores com XX,XX (numeros com virgula)
    info = re.findall(r'[0-9]{1,2}\,[0-9]{1,2}', dado)
    if info:
        return 'VIRG'
    # Procura Grau XX°XX
    info = re.findall(r'[0-9]{1,2}°[0-9]{1,2}', dado)
    if info:
        return 'GRAU'
    info = re.findall(r'[0-9]{1,2}°.[0-9]{1,2}', dado)
    # Procura grau com ponto XX°.XX
    if info:
        return 'GRAUPONTO'
    info = re.findall(r'[a-z]*', dado, flags=re.I)
    # Deixa o resto em texto
    if info:
        return 'TXT'
    if info is None:
        return 'NADA'


def conversao_dado(v):
    res = valid(v)
    if res == 'NUM':
        return v
    if res == 'GRAU':
        new_v = v.replace("'", "")
        return new_v.replace('°', '.')
    if res == 'GRAUPONTO':
        new_v = v.replace('°.', '.')
        return new_v.replace("'", "")
    if res == 'VIRG':
        return v.replace(',', '.')
    if res == 'TXT':
        return v
    res = None

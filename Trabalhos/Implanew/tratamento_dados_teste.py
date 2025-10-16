import re
dados = ["-", "110.90", "11°35'", "13 Voltas", "3.00", "1,95", "8°.00'", "6 Voltas", "P/P", "*19998"]


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


num = []
grau = []
texto = []

for v in dados:
    res = valid(v)
    if res == 'NUM':
        num.append(v)
    if res == 'GRAU':
        new_v = v.replace("'", "")
        grau.append(new_v.replace('°', '.'))
    if res == 'GRAUPONTO':
        new_v = v.replace('°.', '.')
        grau.append(new_v.replace("'", ""))
    if res == 'VIRG':
        num.append(v.replace(',', '.'))
    if res == 'TXT':
        texto.append(v)
    res = None


print(f'NUMEROS >>> {num}')
print(f'GRAU >>> {grau}')
print(f'TEXTOS >>> {texto}')

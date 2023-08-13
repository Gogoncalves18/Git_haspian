def formata_tamanho(tam):
    base = 1024
    kilo = base
    mega = base **2
    giga = base **3
    tera = base **4
    peta = base **5

    if tam < kilo: 
        texto = 'B'
    elif tam < mega:
        tam /= kilo
        texto = 'K'
    elif tam < giga:
        tam /= mega
        texto = 'M'
    elif tam < tera:
        tam /= giga
        texto = 'G'
    elif tam < peta:
        tam /= tera
        texto = 'T'
    else:
        tam /= peta
        texto = 'P'

    tam = round(tam, 2)
    return f'{tam}{texto}'

    
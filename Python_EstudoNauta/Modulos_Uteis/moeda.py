'''Modulo para formatar numeros float com "." para numeros com
 "," na formatação da moeda Real'''


def moeda(vlr):
    """
    Função deve receber um valor numérico com '.' para definir a
    casa decimal ou número inteiro
    """
    try:
        num = float(vlr)
    except ValueError:
        msg = 'Você precisa digitar um valor numérico com ponto ao \
invés de ",". Não digite palavras!'
        return msg
    except TypeError:
        print('Por favor, digite números decimais com ","')
    else:
        resp = f'R${num:.2f}'.replace('.', ',')
        if resp is not None:
            # Necessario adicionar esta condicional senão o valor de
            # resp sempre será lido como None quando nao informo numero
            return resp

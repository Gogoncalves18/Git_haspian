'''Modulo para formatar numeros float com "." para numeros com "," na formatação da moeda Real'''

def moeda(vlr):
    """
    Função deve receber um valor numérico com '.' para definir a casa decimal ou número inteiro
    """
    try:
        num = float(vlr)
    except ValueError:
        print('Você precisa digitar um valor numérico')
    except TypeError:
        print('Por favor, digite números decimais com ","')
    else:
        resp = f'R${num:.2f}'.replace('.',',')
        return resp
    
    

      
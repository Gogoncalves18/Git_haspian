def quickSort(dados):
    if len(dados) < 2:
        return dados
    else:
        pivo = dados[0]
        menores = [i for i in dados[1:] if i <= pivo]
        maiores = [i for i in dados[1:] if i > pivo]
        return quickSort(menores) + [pivo] + quickSort(maiores)

# Programa Principal


dados = [50, 25, 92, 16, 76, 30, 43, 54, 19]
dados = quickSort(dados)
print(dados)
def mergesort(dados):
    if len(dados) > 1:
        meio = len(dados)//2
        esq = dados[:meio]
        dir = dados[meio:]
        mergesort(esq)
        mergesort(dir)

        i = j = k = 0

        while i < len(esq) and j < len(dir):
            if esq[i] < dir[j]:
                dados[k] = esq[i]
                i = i+1
            else:
                dados[k] = dir[j]
                j = j+1
            k = k+1
        while i < len(esq):
            dados[k] = esq[i]
            i = i+1
            k = k+1
        while j < len(dir):
            dados[k] = dir[j]
            j = j+1
            k = k+1

# Main Program


dados = [54, 26, 93, 17, 77, 31, 44, 55]
mergesort(dados)
print(dados)
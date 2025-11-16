# Importacao da biblioteca para construcao do assembly com opcode menor que 4
import dis


# Funcao para chamar a biblioteca do assembly com codigo otimizado
def convert_assemb():

    # Definicao dos Pesos que foram calculados no treinamento da rede
    # neural na tabela excel
    pesos = [0.563157895, 0.503157895, -0.281052632,
             -0.324210526, 0.661052632, -0.189473684]
    # 19 amostras de resultados escolhidos atraves da tabela de amostragem.
    # Os 6 primeiros digistos de cada lista sao os valores lidos pelo sensor,
    # o setimo
    # digito é o resultado experado de saída da funcão ativadora
    amostras = [
        [3, 6, -1, 9, -1, 6, -1],
        [4, 2, 3, -1, -2, 9, -1],
        [2, 2, 0, 1, -2, 7, -1],
        [0, 1, 0, 4, -1, 1, -1],
        [3, 3, 3, 5, 0, 3, -1],
        [-1, -1, 9, 3, 8, -1, -1],
        [2, 7, 4, 2, 6, -2, 1],
        [0, 0, 0, 8, 9, 4, 1],
        [4, 1, 6, 4, -2, -2, -1],
        [-2, 2, -1, 1, -2, -1, -1],
        [4, -2, 4, 2, 0, 4, -1],
        [-2, -2, 7, 2, -1, 5, -1],
        [-1, 2, -1, -2, 9, -2, 1],
        [1, -2, 0, -1, -2, 4, -1],
        [-2, 5, -2, 8, 1, 9, -1],
        [-1, 8, 7, 0, 8, -1, 1],
        [5, -2, 5, -1, 8, 9, 1],
        [9, -1, -2, -2, 6, 7, 1],
        [-1, 2, 6, 5, 1, 5, -1]
    ]

    # loop para rodar as amostras em uma funcão otimizada misturando list
    # comprehension
    # com uma funcao de soma do próprio python para ler cada soma em uma
    # funcao zip do pyhton
    # ao qual estou fatiando apenas os 6 primeiros digitos. Em resumo, pego
    # cada valor de uma lista
    # de amostras e peso, multiplico um pelo outro e somo eles, diminuindo
    # pelo meu valor Bias.
    # Esta funcão permitiu gerar um assembly menor que 4 para cada opcode.
    # Atendendo a exigência do trabalho.
    for linha in amostras:
        # Produto escalar simples
        d1 = sum(x * w for x, w in zip(linha[:6], pesos)) - 1
        fx_ativ = 1 if d1 >= 0 else -1
        print("Saída de Ativação:", fx_ativ, "=>", "Mantenha Produção" if fx_ativ == 1 else "DESATIVAR ESTEIRAS")


dis.dis(convert_assemb)

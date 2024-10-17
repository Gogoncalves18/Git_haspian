from dotenv import load_dotenv
from os import getenv
import os
from openpyxl import load_workbook


load_dotenv()

xls = getenv("table")
xls_path = getenv("loc_xls")
xls_imported = os.path.join(xls_path, xls)

# Carrega o arquivo excel
wb = load_workbook(xls_imported)
# Seleciona a primeira aba
ws = wb.worksheets[0]
# Leitura de linhas utilizadas e gravadas no metadados do arquivo, nao confiar
# neste parametro, necessario interar sobre ele
qtd_rows = ws.max_row

# Parametro para contagem de linha
count_col = 1
count_row = 1
# Param para qtd de colunas + 1
qtd_real_col = 7


# Altera o valor da celula de ACAO
def atual_status(lin):
    ws.cell(row=lin, column=qtd_real_col-2).value = 4


def confirma_importacao(ops_to_excel):
    # Parametro para contagem de linha
    count_col = 1

    # Varre todas linhas (excluindo o cabecalho) da tabela ate o ultima linha
    # do metadado da tabela
    for lin in range(2, qtd_rows+1):
        # Intera sobre o numero de coluna indicado
        for col in range(1, qtd_real_col):
            # Le a celula de cada linha e coluna
            val_cell = ws.cell(row=lin, column=count_col).value
            # Le apenas a primeira coluna e se esta preenchida
            if val_cell is not None and count_col == 1:
                # Regra para encontrar a OF enviada para funcao em uma LIST
                # print(f'LISTA DENTRO DA CONFIRMACAO IMPORT {ops_to_excel}')
                if int(val_cell) in ops_to_excel:
                    print(f'>> Linha {lin} -- Col {col} '
                          f'-- ValCELL {val_cell}')
                    atual_status(lin)
            # Salva apos nao encontrar mais nada na primeira coluna
            if val_cell is None and count_col == 1:
                wb.save(xls_imported)
                break
            # Intera a valor da coluna na mesma linha
            count_col += 1
            # Controlador para validar se e a ultima coluna a ser
            if count_col == qtd_real_col:
                count_col = 1


if __name__ == '__main__':
    confirma_importacao()

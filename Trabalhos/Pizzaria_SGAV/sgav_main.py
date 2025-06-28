from modulos.bckup_banco import Movimentacao_Backups
from dotenv import load_dotenv
from os import getenv

load_dotenv()
path_bck_pdv = getenv("local_origem_bcksql_pdv")
new_path_bck_pdv = getenv("local_destino_bcksql_pdv")
nome_fisco = getenv("nome_bck_fisco")
nome_venda_pdv = getenv("nome_bck_pdv_venda")
nome_venda_cbo = getenv("nome_bck_cbo_venda")
bak_sql_pdv = getenv("bak_sql_pdv")

path_bck_cbo = getenv("local_origem_bcksql_cbo")
new_path_bck_cbo = getenv("local_destino_bcksql_cbo")
bak_sql_cbo = getenv("bak_sql_cbo")

bck_pdv = Movimentacao_Backups(path_bck_pdv, new_path_bck_pdv, nome_fisco,
                               nome_venda_pdv, bak_sql_pdv)

# bck_cbo = Movimentacao_Backups(path_bck_cbo, new_path_bck_cbo, nome_fisco,
#                               nome_venda_cbo, bak_sql_cbo)

# Funcao para executar uma movimentacao de arquivos do bckup, estes
# arquvivos sao salvos pelo Colibri ERP em uma pasta e movimentados
# para outra pasta, extraidos, renomeados e restaurados
bck_pdv.mov_bckup()

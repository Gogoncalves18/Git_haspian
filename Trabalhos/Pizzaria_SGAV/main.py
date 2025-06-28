from infra.repository_bd.modo_venda_rep import Modo_Venda_Repository
from infra.repository_bd.restaurarbd_rep import Restaurar_BD

tipo_venda = Modo_Venda_Repository()

dados = tipo_venda.select()
for dado in dados:
    print(dado)

rest = Restaurar_BD()
rest.restaurar_sql()

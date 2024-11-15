# https://www.youtube.com/watch?v=RoYuIKkGUy8&list=PLYfSsxE6TZLsbszd4qVW114Aftn4aALAa&index=3

# Metodos

class Produto:

	def __init__(self, name, vlr_custo, vlr_venda) -> None:
		self.vlr_custo = vlr_custo
		self.vlr_venda = vlr_venda
		self.name = name

	def calc_lucro(self):
		return (self.vlr_venda - self.vlr_custo)
	
	def prod_preco(self):
		return f'Produto {self.name} custa R${self.vlr_venda:.2f}'


cel = Produto(name="Camisa", vlr_custo=80, vlr_venda=100)
# Implicitamente o py passa para o metodo "calc_lucro()" o obj cel
print(cel.calc_lucro())
print(f'\n{cel.prod_preco()}')

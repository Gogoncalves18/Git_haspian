# https://www.youtube.com/watch?v=RoYuIKkGUy8&list=PLYfSsxE6TZLsbszd4qVW114Aftn4aALAa&index=5

# Heranca de classe
class Pessoa:  # Super Class
	def __init__(self, nome, sobrenome, cpf) -> None:					#4
		self.nome = nome												#5
		self.sobrenome = sobrenome										#6
		self.cpf = cpf													#7

	def obtem_nome_completo(self):
		return f'{self.nome} {self.sobrenome}'
	

class Cliente(Pessoa):  # Sub Class
	def __init__(self, nome, sobrenome, cpf) -> None:					#2
		# Necessario passar para a sub class todos os parametros que	
		# quero que ele receba do pai "nome, sobrenome, cpf"
		super().__init__(nome, sobrenome, cpf)							#3
		self.compras = []												#8


class Funcionario(Pessoa):  # Sub Class
	def __init__(self, nome, sobrenome, cpf, sal) -> None:
		super().__init__(nome, sobrenome, cpf)
		self.salario = sal

	def calc_pagto(self):
		return self.salario - ((10/100) * self.salario)
	

class Programador(Funcionario):
	def __init__(self, nome, sobrenome, cpf, sal, bonus) -> None:
		super().__init__(nome, sobrenome, cpf, sal)
		self.bonus = bonus

	def calc_pagto(self):
		pagt0_sal = super().calc_pagto() + self.bonus
		return pagt0_sal
	

# Ordem de execução da linhas:
c1 = Cliente('Paulo', 'Costa', '123.456.789.90')						#1
f1 = Funcionario('Gustavo', 'Goncalves', '123.987.567.30', 5000)
p1 = Programador('Zé', 'Ricardao', '534.987.236.42', 10000, 200)

print(f'\n{c1.obtem_nome_completo()}')
print(f'{type(c1)}')

# Podemos ver que o funcionario usa um metodo da class pessoa por ter 
# herdado ela e ambos os objetos sao de classes diferentes
print(f'\n{f1.obtem_nome_completo()} possui salario de {f1.calc_pagto()}')
print(f'{type(f1)}')

# O py ira buscar na classe o programador o metodo 'calc_pagto()', se ele
# nao encontrar, ele vai para classe pai e depois para classe avô e assim
# até chegar no ultimo nivel. Mas neste caso montamos um novo metodo mais especifico
# para a class programador, que considera o calculo de salario com bonus
print(f'\n{p1.obtem_nome_completo()} possui salario de {p1.calc_pagto()}')
print(f'{type(f1)}')

# ----------------------------------------------------------------------------------------------------------------------
# Tema 5 parte 1 - Sem builder
# class Casa:
#     def __init__(self, num_quartos=None, num_banheiros=None, tem_garagem=False, tem_jardim=False):
#         self.num_quartos = num_quartos
#         self.num_banheiros = num_banheiros
#         self.tem_garagem = tem_garagem
#         self.tem_jardim = tem_jardim
#
#     def __str__(self):
#         caracteristicas = []
#         if self.num_quartos:
#             caracteristicas.append(f"Número de quartos: {self.num_quartos}")
#         if self.num_banheiros:
#             caracteristicas.append(f"Número de banheiros: {self.num_banheiros}")
#         if self.tem_garagem:
#             caracteristicas.append("Possui garagem")
#         if self.tem_jardim:
#             caracteristicas.append("Possui jardim")
#
#         return ', '.join(caracteristicas)
#
#
# # Construindo uma casa com garagem e jardim
# casa = Casa(num_quartos=3, num_banheiros=2, tem_garagem=True, tem_jardim=True)
# print("Características da casa:", casa)
#
# # Construindo outra casa sem garagem e com 4 quartos
# outra_casa = Casa(num_quartos=4, num_banheiros=3)
# print("Características da outra casa:", outra_casa)
#
# # ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# Tema 5 parte 2 - Com builder
# Classe Casa representa o produto final que queremos construir
class Casa:
    def __init__(self):
        self.num_quartos = None
        self.num_banheiros = None
        self.tem_garagem = False
        self.tem_jardim = False

    def __str__(self):
        caracteristicas = []
        if self.num_quartos:
            caracteristicas.append(f"Número de quartos: {self.num_quartos}")
        if self.num_banheiros:
            caracteristicas.append(f"Número de banheiros: {self.num_banheiros}")
        if self.tem_garagem:
            caracteristicas.append("Possui garagem")
        if self.tem_jardim:
            caracteristicas.append("Possui jardim")

        return ', '.join(caracteristicas)


# Classe Builder para construir a Casa passo a passo
class CasaBuilder:
    def __init__(self):
        self.casa = Casa()

    def set_num_quartos(self, num_quartos):
        self.casa.num_quartos = num_quartos
        return self

    def set_num_banheiros(self, num_banheiros):
        self.casa.num_banheiros = num_banheiros
        return self

    def adicionar_garagem(self):
        self.casa.tem_garagem = True
        return self

    def adicionar_jardim(self):
        self.casa.tem_jardim = True
        return self

    def obter_casa(self):
        return self.casa


# Construindo uma casa com garagem e jardim
builder_casa = CasaBuilder()
casa = builder_casa.set_num_quartos(3).\
                    set_num_banheiros(2).\
                    adicionar_garagem().\
                    adicionar_jardim().\
                    obter_casa()
print("Características da casa:", casa)

# Construindo outra casa sem garagem e com 4 quartos
outra_casa = CasaBuilder().set_num_quartos(4).set_num_banheiros(3).obter_casa()
print("Características da outra casa:", outra_casa)
# ----------------------------------------------------------------------------------------------------------------------

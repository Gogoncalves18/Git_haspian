# https://www.youtube.com/watch?v=RoYuIKkGUy8&list=PLYfSsxE6TZLsbszd4qVW114Aftn4aALAa&index=4

# Static Method e Class Method
class Casa:

    list_casas = []

    def __init__(self, qtd_quarto, qtd_banheiro, qtd_vagas) -> None:
        self.qtd_quarto = qtd_quarto
        self.qtd_banheiro = qtd_banheiro
        self.qtd_vagas = qtd_vagas
        Casa.list_casas.append(self)

    def desc(self):
        return f'A casa possui: {self.qtd_quarto} quartos + {self.qtd_banheiro} '\
               f'banheiros + {self.qtd_vagas} vagas!'

    def __repr__(self) -> str:
        return f'A casa possui: {self.qtd_quarto} quartos + {self.qtd_banheiro} '\
               f'banheiros + {self.qtd_vagas} vagas!'

    # É criado um "classmethod" quando eu tenho um metodo que e da class, isto
    # e, nao faz sentido eu gravar a lista de obj(casas) que eu possuo dentro
    # da minha class e usar um metodo dentro do obj ou do obj, assim eu uso um
    # metodo que é da class pois é a class que possui os obj, neste caso
    # eu uso o CLS no lugar do self.
    @classmethod
    def filtra_quartos(cls, qdt_quartos):
        """Recebe uma qtd de quartos para achar a casa que atende"""
        # Lista do metodo para separar as casas que atendem o filtro
        list_casas_filtradas = []
        for i in cls.list_casas:
            # Este "qtd_quarto" e do obj que estou lendo no momento que possui
            # um atr que e a "qtd_quarto" para comparar com a "qdt_quartos"
            # que recebo dentro do metoda da class
            if i.qtd_quarto >= qdt_quartos:
                # Guardo os obj que encontro na lista da class
                list_casas_filtradas.append(i)
        # Retorno a lista resultado do que foi selecionado para quem esta
        # evocando
        return list_casas_filtradas

    # Static Method é utilizado quando eu uso um method de class porem
    # eu nao preciso usar nenhum atr da class
    @staticmethod
    def is_alto_padrao(c):
        return (c.qtd_quarto > 2)


c1 = Casa(qtd_quarto=2, qtd_banheiro=1, qtd_vagas=1)
c2 = Casa(qtd_quarto=5, qtd_banheiro=2, qtd_vagas=3)
c3 = Casa(qtd_quarto=3, qtd_banheiro=2, qtd_vagas=2)

# Listagem da descricao de todas as casas que foram registradas
for c in Casa.list_casas:
    print(c)


# E necessario eu instaciar o resultado do metodo de class
lista_casas = Casa.filtra_quartos(3)
print(f'\nCasas selecionadas:\n{lista_casas}')
print(f'\nCasas selecionadas:\n{Casa.filtra_quartos(3)}')

# Testando o @staticmethod, isto é, a funcao recebe um atr do meu 
# obj e retorna verdadeiro se o atr "qtd_quarto" é maior que 2,
# que se enquadra apenas na C2 e C3
if Casa.is_alto_padrao(c1) is False:
    print('A não é de alto padrão')
else:
    print('Alto padrão')

if Casa.is_alto_padrao(c2) is False:
    print('A não é de alto padrão')
else:
    print('Alto padrão')

if Casa.is_alto_padrao(c3) is False:
    print('A não é de alto padrão')
else:
    print('Alto padrão')

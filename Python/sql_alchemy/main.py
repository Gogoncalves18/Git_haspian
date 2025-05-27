# Importo da pasta que coordena os comandos sql, para poder 
# instancia-la
from repository_bd.filmes_rep import Filmes_Repository
from repository_bd.atores_rep import Atores_Repository

# Todos os cmds sql estarao instanciados aqui
repo_filmes = Filmes_Repository()
atores = Atores_Repository()

# Insercao no BD
#repo_filmes.insert('Matrix', 'Ação', 2001)

# Dentro desta instancia executo os cmds
dados = repo_filmes.select()
for dado in dados:
    print(dado)
print()
# Exemplo usando o join feito em atores_rep.py
acts = atores.select()
for act in acts:
    print(act)

# Exemplo usando o recurso de relação reversa de filmes para atores
# Este recurso este escrito dentro de filmes_rep.py

respostas = repo_filmes.select()
print()
# Aqui tenho a mesma resposta que o primeiro print
print(respostas)
print()
main_filme = respostas[0]
# Consigo trazer os artistas que fizeram o filme que estou selecionando da lista
print(main_filme.artistas)

parei na aula 6, começar a 7
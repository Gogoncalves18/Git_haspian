from operator import itemgetter
ranking={}
dict_temp={}
nomes={'nome': 'Pedro', 'idade': '25', 'nome': 'Joao', 'idade': '30', 
       'nome': 'Rafa', 'idade': '35', 'nome': 'Pepe', 'idade': '19', 
       'nome': 'robert', 'idade': '65', 'nome': 'rodrigo', 'idade': '21', 
       'nome': 'tais', 'idade': '32'}
ranking=sorted(nomes.items(), key=itemgetter(1))
print(ranking)




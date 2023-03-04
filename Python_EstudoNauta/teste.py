lista=[{'nome': 'Ff', 'num_jogos': 1999, 'gols': [2], 'tot_gols': 2}, {'nome': 'Ll', 'num_jogos': 1999, 'gols': [2, 6], 'tot_gols': 10}]
print(f'-='*30,end='\n')
print(f'\n{"COD":<10}{"JOGADOR":<10}{"GOLS":<10}{"TOTAL GOLS":<10}')
print('-'*42) 
for pos, i in enumerate(lista):
  print(f'{pos:<10}', end='')
  for dado in i.items():
    if dado[0]!= 'num_jogos':
      print(f'{str(dado[1]):<10}', end=' ')
      #print(f'{str(dado):<10}', end='')
  print()
print('-'*42) 
analys=0
while True:
  print(f'\nAnalisar qual jogodor? ')
  analys=int(input('Digite o [ID] ou [999] para sair: '))
  if analys == 999:
    break
  else:
    print(f'O jogador {lista[analys]["nome"]} tem {lista[analys]["num_jogos"]} jogos com a seguinte performance:')
    for part, g in enumerate(lista[analys]["gols"]):
      print(f'Na partida {part}, ele fez {g} gols.')


 



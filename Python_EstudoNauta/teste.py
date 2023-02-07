resp='ini'
sair_prog=False
resp_saida=str(input('\nVc quer continuar? [S] ou [N]')).upper()[0]
while resp_saida not in 'SN':
    resp_saida=str(input('\nDIGITE [S] ou [N]')).upper()[0]
if resp_saida=='N':
        sair_prog is True
        resp_saida='N'
        resp=str('passei pelo NAO')
elif resp_saida=='S':
    sair_prog is False
    resp_saida='S'
    resp=str('passei pelo SIM')
print(f'\n{sair_prog}')
print(f'\n{resp}')
  
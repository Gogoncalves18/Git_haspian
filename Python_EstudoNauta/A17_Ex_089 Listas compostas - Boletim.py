# Programa para capturar o nome e duas notas de varios alunos
# Ao encerrar o input mostrar o ID, Nome e Media do aluno
# Por fim deixar um menu para acessar as notas que comporam a media
resp = 'S'
alunos = []
aluno_temp = []
notas_temp = []
while resp == 'S':  # Neste looping eu adiciono os dados nas
    # listas temp e depois limpo apos copiar para outra lista
    aluno_temp.append(str(input('\nNome do Aluno: ')).upper())
    notas_temp.append(int(input('\nInsira nota 1: ')))
    notas_temp.append(int(input('Insira nota 2: ')))
    aluno_temp.append(notas_temp[:])
    # aqui faco um nivel de lista so para notas que joga dentro
    # da lista que tem o aluno
    alunos.append(aluno_temp[:])
    # aqui componho outra lista com a seguinte estrutura:
    # [[aluno,[nota1, nota2]],[aluno,[nota1, nota2]]]
    aluno_temp.clear()
    notas_temp.clear()
    resp = str(input('Continuar? [S] ou [N]')).upper()[0]
print('-='*20)
print(f'{"ID":<10}{"NOME":<10}{"MEDIA":<5}')
print('-'*40)
cont = 0
med = 0
for aluno in alunos:  # printo todos os alunos
    for v in alunos[cont][1]:  # monto a media de cada aluno
        med += v
    print(f'{cont:<10}{alunos[cont][0]:<10}{med/2:<5}')
    cont += 1
    med = 0
print('-'*40)
show_id = 0
while show_id != 999:
    # Solicito se deseja ver as notas que compoem a media, apontando
    # o ID do aluno
    show_id = int(input('\nDigite o ID do aluno para apresentar as \
notas ou [999] para SAIR: '))
    if show_id >= 0 and show_id <= 998:
        print(f'''As notas de {alunos[show_id][0]} sao \
{alunos[show_id][1]}''')
print(alunos)

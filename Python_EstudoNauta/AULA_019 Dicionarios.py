# Declaracao de dicionarios
dados = {}
dados = {'nome': 'Pedro', 'idade': '25'}
cadastro = [{'nome': 'Pedro', 'idade': '25'},
            {'nome': 'Joao', 'idade': '30'},
            {'nome': 'Rafa', 'idade': '35'},
            {'nome': 'Pepe', 'idade': '19'},]

# Extrair dados do dicionario
print(f'LINHA 6 - {dados["nome"]}')
print(f'LINHA 7 - {dados["idade"]} anos')

# Adicionar elementos no dicionario
dados['sexo'] = 'M'
dados['cor'] = 'branco'
print(f'LINHA 12 - {dados}')

# Apagar elemento do dicionario:
del dados['cor']
print(f'LINHA 16 {dados}')

# Acessar items na lista que contem dict
for i in cadastro:
    print(f'LINHA 24 - {i}')

# Acessar os dados do dict que esta na lista
print(f'\n{cadastro}')
print(f'\nLINHA 28 - O {cadastro[1]["nome"]} tem {cadastro[1]["idade"]}\
       anos.')

# Rodar as informacoes dict dentro da list:
print('ABAIXO LINHA 34:')
for i in cadastro:
    for k, v in i.items():  # ITEM É O CONJUNTO DE KEY E VALUE
        print(f'\n{k.title()} = {v}')

# Rodar apenas as keys que estao dentro de um dict que esta dentro
# de uma list:
for i in cadastro:
    print(f'\nLINHA 38 - O Nome é {i["nome"]} e tem {i["idade"]}')

# Apresentar as keys e values de um dict
print(f'\nLINHA 41 - {dados.keys()}')
print(f'\nLINHA 42 - {dados.values()}')
print(f'\nLINHA 43 - {dados.items()}')

# Alimentar uma lista atraves de varias entradas de dict{}:
for c in range(0, 3):
    dados["nome"] = input('\nDigite nome: ')
    dados["idade"] = input('\nDigite idade: ')
    cadastro.append(dados.copy())  # necessario fazer a copiada do
    # dict para dentro da lista em cada laco para nao sobreesrever
print(f'LINHA 52 - {cadastro}')

'''
Programa para tratar niveis de pastas e arquivo analisando informações entre a 
tabela csv e manipulando as pastas de último nível. Segue orientações nos
seguintes passos:

# 1 - Problema a ser tratado: 
A base dos arquivos originais possuem um endereço,
conforme o exemplo: 'C:\Users\gogon\Documents\Inga\tornos', dentro deste
endereço há tipos de máquinas com os seguintes nomes [DOOSAN 2 E 3   2100L,
DOOSAN 2100 PLACA 180, DOOSAN PUMA GT 2100, gl250, gl280, gl280m, Z - MAT TN600].

Estas máquinas precisam ser renomeadas manualmente para os seguintes nomes,
antes de rodar o programas: [DOOSAN 2100L 01_02,
DOOSAN 2100, DOOSAN PUMA GT 2100, GL250, GL280, GL280M, Z - MAT TN600]

Este nível de pasta se chama PONTO_ZERO.

Dentro do ponto zero, em cada máquina, há pastas ao qual seu nome está definido
pelo CODIGO de MERCADO, escrito com diversos caracteres diferentes separando as
vezes CODIGO de MERCADO diferentes no mesmo nome de pasta. Este códigos serão
varridos para identicar cada um deles considerando a varredura para separação
destes códigos por: "_" ou "-" ou "(" ou ")" ou "," quando encontrado no nome
da pasta e ainda é avaliado o mesmo código sem o último caracter para analisar
se bate com os códigos de mercado. Na validação seguinte, após minerar os dados,
ainda é feito nova avaliação separando os dados por "." para encontrar novos 
códigos por este caracter e então validar com a lista csv.

Dentro de cada pasta há os arquivos originais com código de mercado ou nomes 
que não possuem referência alguma com os códigos de mercado.

# 2 - CSV com os códigos interno e de mercado em duas colunas: 

Necessário salvar um CSV dentro de C:\\Users\\gogon\\Documents\, um arquivo
chamado inga.csv ao qual será a base comparativa do programa para manipulação
das pastas e arquivos. Este CSV deverá conter na primeira linha os Nomes de 
cada coluna, os dados deverão estar separados por ";" e cada linha deverá ter 
dois dados sendo o codigo interno (código ao qual o cliente gostaria que os 
arquivos fossem renomeados) como primeiro dado de cada linha e o CODIGO de
MERCADO (nomes que o cliente usa nas pastas) como o segunda dado de cada linha.

# 3 - Local dos novos dados:
Todos os dados serão salvos no endereço: C:\Users\gogon\Documents\Inga\NOVOS tornos

# 4 - Repetir o mesmo procedimento dentro da pasta de Centro de Usinagem
com os seguintes nomes de pasta das máquinas:
[Z - MAT VCM1050E, PAN MACHINE TN1000i, GX 1600 PLUS, CENTRO DUPLO PALLETE HC400,
33 Pallet 1, 33 Pallet 2]

'''
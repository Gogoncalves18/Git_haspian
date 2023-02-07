import random
print ('-'*30)
print ('\nQuais serao os quatros alunos que apresentarao?')
aln1 = str(input('\nNome do primeiro aluno: '))
aln2 = str(input('\nNome do segundo aluno: '))
aln3 = str(input('\nNome do terceiro aluno: '))
aln4 = str(input("\nNome do quarto aluno: "))
list_aln = [aln1, aln2, aln3, aln4]
print (list_aln)
random.shuffle(list_aln)
print (list_aln)

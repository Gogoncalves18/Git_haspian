#Digite um numero de 0 a  20 e apresente o nome por extenso deste numero usando a tecnica de tupla
num=int(input('\nDigite um numero entre 0 e 20:'))
desc_num=('Zero','Um','Dois','Tres','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze',
'Doze','Treze','Quatorze','Quinze','Dezeseis','Dezesete','Dezoito','Dezenove','Vinte')
while True:
    if num>=21:
        num=int(input('\nVc precisa digitar um numero de 0 a 20: '))
    else:
        print(f'\nVc digitou o {num} que escrito por extenso fica {desc_num[num]}')
        break
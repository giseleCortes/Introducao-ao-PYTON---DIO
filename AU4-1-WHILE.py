# WHILE
#força a repetição até que a condição se cumpra.
# no caso abaixo os numero serão imprimidos enquando forem menor ou = a 10

a = 0
while a <= 10:
    print(a)
    a += 1
#-----------------------------------------------------------------------------------

a = int(input('Primeiro Bimestre: '))
while a > 10:
    a = int(input('Voce Digitou errado. Primeiro Bimestre: '))
b = int(input('Segundo Bimestre: '))
while b > 10:
    b = int(input('Voce Digitou errado. Segundo Bimestre: '))
c = int(input('Terceiro Bimestre: '))
while c > 10:
    c = int(input('Voce Digitou errado. Terceiro Bimestre: '))
d = int(input('Quarto Bimestre: '))
while d > 10:
    d = int(input('Voce Digitou errado. Quarto Bimestre: '))

media = (a+b+c+d)/4
if a <= 10 and b <= 10 and c <= 10 and d <= 10:
    print('média: {}'.format(media))
else:
    print('Foi informado algum valor inválido')

#correção do erro no codigo da aula AU3-1

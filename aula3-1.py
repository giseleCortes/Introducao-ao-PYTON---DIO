a = int(input('Primeiro Bimestre: '))
b = int(input('Segundo Bimestre: '))
c = int(input('Terceiro Bimestre: '))
d = int(input('Quarto Bimestre: '))

media = (a+b+c+d)/4
print('média: {}'.format(media))
if a <= 10 and b <= 10 and c <= 10 and d <= 10:
    print('média: {}'.format(media))
else:
    print('Foi informado algum valor inválido')

#OU

a = int(input('Primeiro Bimestre: '))
if a > 10:
    a = int(input('Voce Digitou errado. Primeiro Bimestre: '))
b = int(input('Segundo Bimestre: '))
if b > 10:
    b = int(input('Voce Digitou errado. Segundo Bimestre: '))
c = int(input('Terceiro Bimestre: '))
if c > 10:
    c = int(input('Voce Digitou errado. Terceiro Bimestre: '))
d = int(input('Quarto Bimestre: '))
if d > 10:
    d = int(input('Voce Digitou errado. Quarto Bimestre: '))

media = (a+b+c+d)/4
print('média: {}'.format(media))
if a <= 10 and b <= 10 and c <= 10 and d <= 10:
    print('média: {}'.format(media))
else:
    print('Foi informado algum valor inválido')


# mas esse código tem um erro, se digitar errado uma segunda fez ele passa para a proxima opção
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

if a > b and a > c:
    print('O maior numero é: {}'.format(a))
elif b > a and b > c: #
    print('O maior numero é: {}'.format(b))
else:
    print('O maior numero é: {}'.format(c))

print('Programa Finalizado')

# Em python a identação finaliza um bloco. Diferente de  outras linguagens onde voce deve utilizar ponto e virgula
# por exemplo para finalizar um bloco. Por exemplo "print ('Programa finalizado') sera escrito independente se a for
# maior que b pois está fora do bloco do if em função do espaço (( 4 espaços) o tab faz isso automaticamente)

a = int(input('Entre com um valor: '))
resto = a % 2
if resto == 0:
    print('Nuúero é par.')
else:
    print('Número é impar.')

print('Programa Finalizado')

a = int(input('Entre com primeiro valor: '))
b = int(input('Entre com segundo valor: '))

resto_a = a % 2
resto_b = b % 2
if resto_a == 0 or resto_b == 0:
    print('Foi digitado um numero par ')
else:
    print('Nenhum numero par foi digitado')

print('Programa Finalizado')

a = int(input('Entre com primeiro valor: '))
b = int(input('Entre com segundo valor: '))

#O not ele inverte a operação deixa de ser se isso for verdadeiro para, se isso for falso

resto_a = a % 2
resto_b = b % 2
if resto_a == 0 or not resto_b > 0:
    print('Foi digitado um numero par ')
else:
    print('Nenhum numero par foi digitado')

print('Programa Finalizado')


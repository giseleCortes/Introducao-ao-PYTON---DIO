a = 10
b = 6
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
#para saber o tipo da variavel utilizamos a função type
print(type(soma))

#para converter o tipo da variavel para texto utilizamos str
soma =str(soma)
print(type(soma))
print ('soma: '+ str(soma))
print(soma)
print(subtracao)
print(multiplicacao)
print(divisao)
print(resto)
a = 10
b = 6
#para convertermos o tipo  da variavel para inteiro utilizamos int
print(type(divisao))
print(divisao)
print (int(divisao))
x = 1
soma2 = int(x) + 1

# Em python a forma ideal para cocatenar tipos diferentes de variaveis é utilizando o .format
x = 15
y = 10
soma = x + y
subtracao = x-y
multiplicacao = x * y
divisao = x / y
resto = x % y
print('Soma: {} Subtração: {}'.format(soma, subtracao))
print ('Soma: {adicao} Subtração:{sub}' .format(adicao=soma, sub=subtracao))
print ('Soma: {adicao} \nSubtração:{sub} \nMultiplicação: {mult} \nDivisão: {div} \nResto: {sobra}'
       .format(adicao=soma, sub=subtracao, div=divisao, sobra=resto, mult=multiplicacao ))
# quando atribuimos entre chaves a ordem em format se torna irrelevante ele sempre irá "printar" corretamente
# independente da ordem

# Intereção com usuário

# É preciso converter a variavel para inteiro pois ela é considerada uma string

a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
print (type(a))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
print ('Soma: {adicao} \nSubtração:{sub} \nMultiplicação: {mult} \nDivisão: {div} \nResto: {sobra}'
       .format(adicao=soma, sub=subtracao, div=divisao, sobra=resto, mult=multiplicacao ))

#OU

resultado = ('Soma: {adicao} \nSubtração:{sub} \nMultiplicação: {mult} \nDivisão: {div} \nResto: {sobra}'
       .format(adicao=soma, sub=subtracao, div=divisao, sobra=resto, mult=multiplicacao ))



print(resultado)


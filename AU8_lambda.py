# def contador_letras(lista_palavras):
#     contador = []
#     for x in lista_palavras:
#         quantidade = len(x)
#         contador.append(quantidade)
#     return contador
#
# if __name__ == '__main__':
#     lista = ['cachorro', 'gato']
#     print(contador_letras(lista))

# mesmo codigo feito com lambda
# lambda é uma função anonima que é utilizada para simplificar o que vai ser utilizado mais de uma vez no codigo
# a função abaixo tem a mesma função do codigo acima
# lambda não pode ser utilizado em todos as funções apenas nas mais simples que dê para resolver em apenas uma linha

contador_letras = lambda lista: [len(x) for x in lista]


lista = ['cachorro', 'gato']
print(contador_letras(lista))

soma = lambda a, b: a + b
subtracao = lambda a, b: a - b

print(soma(5, 10))
print(subtracao(10, 5))

# dicionário de funções lambda

calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b,
}

print(type(calculadora))
soma = calculadora['soma']
multiplicacao = calculadora['multiplicacao']
# soma = lambda a, b: a + b ( acima equivale a isso) pois a função é a propria variavel eu não preciso dar um nome pra ela
# por isso ela é uma funçao anonima
print('A soma é: {}' .format(soma(10, 5)))
print('O resultado da multiplicação é: {}' .format(multiplicacao(5, 500)))

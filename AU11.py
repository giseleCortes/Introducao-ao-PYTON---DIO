# É importante, pois se houver um erro em alguma parte do codigo, um erro prvisto ou não previsto. Pode se
# utilizar o try/except para que o codigo continue e depois aquele erro tratado


lista = [1, 10]
arquivo = open('teste.txt', 'r')
try:
    texto = arquivo.read()
    divisao = 10 / 0
    # divisao = 10 / 1
    # numero = lista[3]
    numero = lista[1]
    # x = a
except ZeroDivisionError:
    print('Não é possivel realizar divisão por zero')
except IndexError:
    print('Erro ao acessar um indice inválido da lista')
except BaseException as ex:  # pode utilizar apenas exception
    print('Erro Desconhecido. Erro {}'.format(ex))
# A lista de exceçao é hierarquica, e a ordem em que elas são colocadas tem importancia sim.
# Verificar na documentação do python Exception hierarchy
else:
    print('Executa o código, quando não ocorre exceção')
finally: # geralmente quando ocorre um erro antes o codigo para de ser executado. Neste caso
    # mesmo com o erro da divisão o arquivo sera fechado
    print('Sempre executa')
    arquivo.close()
# Ou seja, quando voce depender que o codigo não tenha nenhum erro nas exceções utilize esse else.
# Se houver algum erro no bloco ele não seguirá para o else
# no caso a frase não será impressa

#Tuplas são imutaveis. Diferente das listas são declaradas entre chaves

tupla_exemplo = (2, 4, 6, 8, 10)
print(tupla_exemplo)

#tambem podemos verificar quantos elementos(indices) tem em uma tupla

print(len(tupla_exemplo))

#COMO convertemos uma lista para tupla TUPLE

lista_animais = [ 'cachorro', 'gato', 'jacaré', 'tatu']
print(lista_animais)

print(type(lista_animais))

tupla_animais = tuple(lista_animais)
print(tupla_animais)

#Como convertemos uma tupla para lista LIST

lista_numerica = list(tupla_exemplo)
print(lista_numerica)
print(type(tupla_exemplo))
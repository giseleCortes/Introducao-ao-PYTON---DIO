conjunto = {1, 2, 3, 4, }
print(conjunto)
# set é conjunto em ingles
print(type(conjunto))

# O conjunto não aceita duplicidade de elementos independente da ordem que ele aparece
conjunto1 = {1, 1, 2, 2, 3, 3, 3, 4, }
print(conjunto1)

# permite a adição de elementos
conjunto.add(5)
print('Adicionando um item do conjunto: {}'.format(conjunto))

# permite a exclusão de elementos
conjunto.discard(5)
print('Removendo um item do conjunto: {}'.format(conjunto))

# esses conjuntos equivalem aos conjuntos aritimeticos, e assim como eles permitem união de conjuntos

conjuntoA = {1, 2, 3, 4, }
conjuntoB = {4, 5, 6, 7, 8, }

uniao_conjuntos = conjuntoA.union(conjuntoB)
print('União entre A e B: {}' .format(uniao_conjuntos))  # retira a duplicidade

uniao_conjuntos = conjuntoB.union(conjuntoA)
print('União entre B e A: {}'.format(uniao_conjuntos))
print('A ordem dos fatores não altera o produto')
# como podemos ver no caso acima a ordem dos fatores não altera o produto rsrs
# é possivel tbm fazer a interseccao dos conjuntos
# interseccao é tudo que se repete nos conjuntos
interseccao_conjunto = conjuntoA.intersection(conjuntoB)
print('Intersecção entre A e B: {}'.format(interseccao_conjunto))
interseccao_conjunto = conjuntoB.intersection(conjuntoA)
print('Intersecção entre B e A: {}'.format(interseccao_conjunto))
print('A ordem dos fatores não altera o produto')
# No caso acima também a ordem dos fatores não altera o produto.
# é possivel realizar a diferença dos conjuntos
diferenca_conjunto = conjuntoA.difference(conjuntoB)
print('Diferença entre A e B: {}'.format(diferenca_conjunto))
diferenca_conjunto = conjuntoB.difference(conjuntoA)
print('Diferença entre B e A: {}'.format(diferenca_conjunto))
print('A ordem dos fatores altera SIIM o produto')
# no caso acima SIIM a ordem dos fators altera o produto.
# diferença simetrica, tras tudo que é não se repete nos conjuntos
conjunto_diff_simetrica = conjuntoA.symmetric_difference(conjuntoB)
print('Diferença Simétrica: {}'.format(conjunto_diff_simetrica))
conjunto_diff_simetrica = conjuntoB.symmetric_difference(conjuntoA)
print('Diferença Simétrica: {}'.format(conjunto_diff_simetrica))
print('Retirou o 4 o elemento que se repetia em ambos conjuntos')







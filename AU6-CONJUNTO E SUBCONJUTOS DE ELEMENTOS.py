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
print('União entre A e B: {}'.format(uniao_conjuntos))  # retira a duplicidade

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

# subset  .issubset
# utilizado para saber se um conjunto pertence a outro

conjunto_A = {1, 2, 3}
conjunto_B = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_A.issubset(conjunto_B)
print('A é um subconjunto de B: {}'.format(conjunto_subset))
# sim os elementos do conjuto A estão dentro do conjunto B, mas e ao contrário?
conjunto_subset = conjunto_B.issubset(conjunto_A)
print('B é um subconjunto de A: {}'.format(conjunto_subset))
# não porque ha elementos no conjunto B que não fazer parte do conjunto A

# superset .issuperset
# é meio que ao contrário do que acontece no subset

conjunto_superset = conjunto_B.issuperset(conjunto_A)
print('B é um superconjunto de A: {}'.format(conjunto_superset))
# sim o conjunto B é um superconjunto do conjunto A pois ele tem todos os elementos do conjunto A
conjunto_superset = conjunto_A.issuperset(conjunto_B)
print('A é um superconjunto de B: {}'.format(conjunto_superset))

# Como converter uma lista em conjunto
# pode ser utilizado para retirar duplicidade de dados




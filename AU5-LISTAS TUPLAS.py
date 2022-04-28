lista = [1, 3, 5, 7]
lista_animal =['cachorro', 'gato', 'elefante']
print(lista)
print(lista_animal[0]) #utilizando indices, nesse caso ele vai imprimir apenas a informação no indice
                       # declarado entre os colchetes

# imprimindo todos os elementos da lista
for y in lista_animal:
    print(y) #x passa a ser um elemento da lista sempre que o laço se repetir. Nesse caso o laço
             # se repete 3x pois na lista tem 3 indices 0,1,2

#SOMANDO OS ELEMENTOS DA LISTA
soma = 0
for x in lista:
    print(x)
    soma += x
print (soma)
#ou ainda
print(sum(lista))   # apenas se os elementos da lista forem no mesmo tipo se a lista fosse lista = [1, 2, flor]
                    # sum não funcionaria

print(max(lista))   # para verificar o maior e o menor numero dentro de uma lista, indenpendente da posição
print(min(lista))
#funciona tbm com strings ele vai trazer o menor e o menor indice baseado na ordem alfabética
print(max(lista_animal))
print(min(lista_animal))

#pode multiplicar os elementos de uma lista de strings

nova_lista = lista_animal * 3
print(nova_lista)

# Pode procurar um elemento na lista
a = str(input('Digite um animal: '))
if a in lista_animal:
    print('Exite essa animal na lista')
else:
    print('Não existe esse animal na linha')
# e ainda incluir o elemento pesquisado na lista utilizando  .append()
    lista_animal.append(a)
    print(lista_animal)
    print('Animal incluido')

# ou excluir com .pop()

lista_animal.pop() # sem declarar o indice a .pop irá exluir a ultima posição
print(lista_animal)

lista_animal.pop(2) #declarando ele segue o indice(da lista original nesse caso aqui)
print(lista_animal)
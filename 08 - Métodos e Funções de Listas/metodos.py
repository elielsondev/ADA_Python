# Métodos de Listas

lista = [1, 3, 15, 30]

novo_numero = 45

# append
print('Antes do append: ', lista)
# Antes do append:  [1, 3, 15, 30]

lista.append(novo_numero)

print('Depois do append: ', lista)
# Depois do append:  [1, 3, 15, 30, 45]


# insert
# lista.insert(posicao_do_indice, item_a_ser_inserido)
print('Antes do insert:', lista)
# Antes do insert: [1, 3, 15, 30, 45]

lista.insert(3, 22)

print('Depois do insert:', lista)
# Depois do insert: [1, 3, 15, 22, 30, 45]


# extend
print('Antes do extend:', lista)
# Antes do extend: [1, 3, 15, 22, 30, 45]

lista2 = [0, -10, -5]

lista.extend(lista2)

print('Depois do extend:', lista)
# Depois do extend: [1, 3, 15, 22, 30, 45, 0, -10, -5]


# pop
print('Antes do pop:', lista)
# Antes do pop: [1, 3, 15, 22, 30, 45, 0, -10, -5]

# Remove o último item da lista
lista.pop()

print('Removido o último item da lista:', lista)
# Removido o último item da lista: [1, 3, 15, 22, 30, 45, 0, -10]

# Remove o item no indice definido
# lista.pop(indice)
lista.pop(4)

print('Removido o item da lista no indice 4 da lista:', lista)
# Removido o item da lista no indice 4 da lista: [1, 3, 15, 22, 45, 0, -10]
# O 30 foi removido


# remove
# Remove o primeiro valor definido no parametro, encontrado na lista
print('Lista antes do remove:', lista)
# Lista antes do remove: [1, 3, 15, 22, 45, 0, -10]

lista.remove(15)
print('Removendo o valor 15 da lista:', lista)
# Removendo o valor 15 da lista: [1, 3, 22, 45, 0, -10]

# count
print('Lista atualizada:', lista)
# Lista atualizada: [1, 3, 22, 45, 0, -10]

print('Tem quantos 22 na lista:', lista.count(22))
# Tem quantos 22 na lista: 1

# index
print('Qual é o indice do elemento 45:', lista.index(45))
# Qual é o indice do elemento 45: 3

# sort

# Ordem crescente
lista.sort()

print(lista)
# [-10, 0, 1, 3, 22, 45]

# Ordem decrescente
lista.sort(reverse=True)

print(lista)
# [45, 22, 3, 1, 0, -10]

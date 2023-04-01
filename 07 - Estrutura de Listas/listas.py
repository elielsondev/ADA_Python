# > Listas

# Antes
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

# Com lista
notas = [7.9, 9.7, 8.2]

# Criando Listas
lista = []
lista = list()
lista = [32, 'Elielson', 1.80, True]
lista_de_listas = [12, ['a', 'b', 'c'], [1, 2, 3]]

# Indexação e Slices (fatiamento)
lista = [32, 'Elielson', 1.80, True]

# Acessando cada item da lista sem o for ou while:
print()
print('SEM LAÇO DE REPETIÇÃO')

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

# Acessando cada item da lista com o for:
print()
print('COM FOR')

# for i in range(len(lista)):
#     print(lista[i])

for item in lista:
    print(item)


# Acessando cada item da lista com o while:
print()
print('COM WHILE')

i = 0

while i < len(lista):
    print(lista[i])
    i += 1

print()

# Slices
lista = [10, 50, 30, 40, 25, 60, 5]

print(lista[0:3])  # Começa no indice 0 e termina antes do indice 3
# [10, 50, 30]

print(lista[3:6])  # Começa no indice 3 e termina antes do indice 6
# [40, 25, 60]

print(lista[3:])  # Começa no indice 3 até o final
# [40, 25, 60, 5]

print(lista[2:6:2])
# Começa no indice 2 e termina antes do 6, "pulando" de 2 em 2
# [30, 25]

print(lista[:])
[10, 50, 30, 40, 25, 60, 5]

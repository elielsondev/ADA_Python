# Laço de Repetição com FOR

for index in range(1, 11, 3):
    print(index)
    index += 1

'''
OBS: O range() possui algumas caracteristicas interessantes:

- range(10) com 1 parametro, vai de 0 até o número antecessor do que está
inserido nele, ou seja, nesse exemplo será: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

- range(1, 10) com 2 parametros o primeiro parametro define onde ele deve
iniciar e o segundo parametro é o 'ponto de corte': 1, 2, 3, 4, 5, 6, 7, 8, 9

range(1, 11, 3) com 3 parametros o que muda aqui em relação ao range de
2 parametros é que o terceiro parametro é definido para "pular" números
ex: 1, 4, 7, 10
'''

soma_nota = 0

for i in range(1, 5):
    nota = float(input(f'Informe a sua nota{i}: '))
    soma_nota = soma_nota + nota

media = soma_nota / 4

print(f'Sua média foi: {media}')

if media >= 7:
    print('APROVADO!')
elif media >= 5:
    print('RECUPERAÇÃO!')
else:
    print('REPROVADO!')

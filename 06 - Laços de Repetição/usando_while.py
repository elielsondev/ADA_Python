# Laço de Repetição com WHILE

# Criando um sorteio com o WHILE:
# Números de 1 a 10:
numero_sorteado = 9
numero_escolhido = int(input('Escolha um número de 1 a 10 e Boa Sorte! '))

while numero_escolhido != numero_sorteado:
    print('Você errou, tente novamente!')
    numero_escolhido = int(input('Escolha um número de 1 a 10 e Boa Sorte! '))

print('PARABÈNS, VOCÊ ACERTOU!!!')


# Incrementando o contador:
num = 6
contador = 0

while contador < num:
    print(contador)
    # contador = contador + 1
    contador += 1

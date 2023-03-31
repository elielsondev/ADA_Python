# > VARIÀVEIS

# 1. Variáveis

idade = 26  # Criando uma variável

print(idade)

nome = 'Elielson Nascimento'

print(nome)

'''
  Tipos de variáveis

  1. int: números inteiros, ou seja, números sem parte decimal: 0, 5, -1, 1000
  2. float: números reais, ou seja, números com parte decimal: 1.0, -2.7, 3.14
  3. str: cadeias de caracteres, ou seja, dados textuais (string)
  4. bool: valores lógicos (booleanos): True ou False
'''

ano_nascimento = 1990

altura = 1.80

nome_completo = 'Elielson do Nascimento Ramos'

estudando = True

print(type(ano_nascimento))  # <class 'int'>
print(type(altura))  # <class 'float'>
print(type(nome_completo))  # <class 'str'>
print(type(estudando))  # <class 'bool'>

# Obtendo dados do usuário e salvando em variáveis

linguagem = input('Qual a linguagem de programação que você está estudando? ')

# Imprimindo variáveis + Mais sobre a função print
print('A linguagem que você está estudando é: ', linguagem)

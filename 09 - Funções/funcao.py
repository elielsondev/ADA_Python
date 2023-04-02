# > Funções

# 1. O que são funções e por que utilizá-las?

# Funções que já utilizamos anteriomente ....

# print() - Imprimi uma mensagem (int, float, str) no console (terminal, cmd)

'''
input() - Retorna um dado informado pelo usuário (entrada padrão) e pode
receber uma string
'''

# len() - Recebe uma lista e retorna o tamanho dessa lista.

# max() - Retorna o maior elementode uma lista.

# 2. Criação de Funções

# Função inicial


def saudacao():
    print("Seja bem-vinda(o)!")
    print("Olá, é um prazer ter você fazendo parte desse curso!")


saudacao()

# Função com parâmentros - Definindo parâmetros para função através de
# variáveis.


def saudacao(nome, curso):
    print(f"Seja bem-vinda(o), {nome}!")
    print(f"Olá, é um prazer ter você fazendo parte desse curso de {curso}!")


saudacao("Paulo Barros", "Python")
saudacao("Isabela", "Solda MIG e MAG")

# Função com parâmetros default - Por default podemos especificar um parâmetro
# para uma determinada variável. Ou altera o default na saida da função.


def saudacao(nome, curso="Python"):
    print(f"Seja bem-vinda(o), {nome}!")
    print(f"Olá, é um prazer ter você fazendo parte desse curso de {curso}!")


saudacao("Paulo Barros", "C++")

# Funções com retorno


def soma(num1, num2):
    # print('Soma =', num1 + num2)
    return num1 + num2


resultado = soma(5, 7)

print("O resultado da soma é", resultado)


def calculadora(num1, num2, operacao="+"):
    if operacao == "+":
        return num1 + num2
    elif operacao == "-":
        return num1 - num2


resultado = calculadora(10, 20, "-")

print(resultado)

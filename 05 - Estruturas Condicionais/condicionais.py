# > Estruturas Condicionais

# 1) Exercício:
# Verificando se a pessoa é maior de idade ou não:
idade = 20

if idade >= 18:
    print('Você é maior de idade.')
else:
    print('Você é menor de idade.')

# 2) Exercício:
'''
  Imagine que você queira imprimir "Aprovado(a)",
  caso o estudante tenha uma média superior ou igual a 7,
  se a média for maior que 5 e menor que 7 fica de "Recuperação",
  e "Reprovado(a)", caso a média seja inferior a 5.
'''
nota1 = float(input('A primeira nota foi? '))
nota2 = float(input('A segunda nota foi? '))
nota3 = float(input('A terceira nota foi? '))
nota4 = float(input('A quarta nota foi? '))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7:
    print('Aprovado(a)!, Sua média foi:', media)
elif media >= 5:
    print('Recuperação!, Sua média foi:', media)
else:
    print('Reprovado(a)!, Sua média foi:', media)

# 3) Exercício

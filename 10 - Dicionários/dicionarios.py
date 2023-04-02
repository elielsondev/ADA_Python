# > Dicionário

# Criando Dicionários
dicionario = {}
dicionario = dict()

dicionario = {
    'nome': 'Elielson',
    'idade': 32,
    'altura': 1.80
}

print(dicionario)
print()

print('DICIONÁRIO SEM O FOR:')
print(dicionario['nome'])
print(dicionario['idade'])
print(dicionario['altura'])
print()


print('DICIONÁRIO COM O FOR:')
for chave in dicionario:
    print(chave, dicionario[chave])
print()

# Adicionando elementos em um dicionário
print('Adicionando e sobreescrevendo item no dicionário:')
dicionario['programador'] = True

print(dicionario)
# {'nome': 'Elielson', 'idade': 32, 'altura': 1.8, 'programador': True}

# Sobreescrevendo um item no dicionário
dicionario['nome'] = 'João'

print(dicionario)
# {'nome': 'João', 'idade': 32, 'altura': 1.8, 'programador': True}
print()

# Testando a existência de uma chave
print('Testando a existência de uma chave no dicionário')
print('peso' in dicionario)  # False
print('altura' in dicionario)  # True

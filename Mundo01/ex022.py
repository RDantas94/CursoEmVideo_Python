# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas
# Quantas letras ao todo(sem considerar espaços)
# Quantas letras tem o primeiro nome
nome = str(input('Digite seu nome completo: '))
nomePartes = nome.split()
primeiroNome = nomePartes[0]
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome possui {len(nome.replace(' ', ''))} letras.')
print(f'Seu primeiro nome é {primeiroNome} possui {len(primeiroNome)} letras.')

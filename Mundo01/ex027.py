# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
nomeCompleto = input('Digite seu nome completo: ')
nome = nomeCompleto.split()
print(f'Primeiro nome: {nome[0]}')
print(f'Último nome: {nome[-1]}')

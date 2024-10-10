# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"
cidade = str(input('Digite o nome de uma cidade: '))
lista = cidade.split()
cidade1 = lista[0]
print(f'A cidade começa com Santo: {'SANTO' in cidade1.upper()}')

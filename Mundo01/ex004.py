# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela.

a = input('Digite algo: ')
print(f'O tipo primitivo do valor digitado é: {type(a)}')
print('Só contem espaços: ', a.isspace())
print('É alfabético: ', a.isalpha())
print('É número: ', a.isnumeric())
print('É alfanumérico: ', a.isalnum())
print('É minúsculo: ', a.islower())
print('É maíusculo: ', a.isupper())
print('É capitalizado: ', a.istitle())

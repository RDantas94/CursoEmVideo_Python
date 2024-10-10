# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada
n = int(input('Digite um número: '))
frase = f'TABUADA DE {n}'
frase2 = 'FIM DA TABUADA'
print(f'{frase:=^35}')
print(f'{n} x 1 = {n}\n'
      f'{n} x 2 = {n*2}\n'
      f'{n} x 3 = {n*3}\n'
      f'{n} x 4 = {n*4}\n'
      f'{n} x 5 = {n*5}\n'
      f'{n} x 6 = {n*6}\n'
      f'{n} x 7 = {n*7}\n'
      f'{n} x 8 = {n*8}\n'
      f'{n} x 9 = {n*9}\n'
      f'{n} x 10 = {n*10}\n')
print(f'{frase2:=^35}')

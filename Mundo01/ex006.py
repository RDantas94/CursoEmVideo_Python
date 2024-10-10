# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
from math import sqrt
n = float(input('Digite um número: '))
d = n * 2  # Dobro
t = n * 3  # Triplo
r = sqrt(n)  # Raiz quadrada
print(
    f'o número {n} tem como seu dobro o valor {d},\nseu triplo {t} \ne sua raiz quadrada {r:.2f}')

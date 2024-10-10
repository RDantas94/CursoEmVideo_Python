# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
from math import cos, sin, tan, radians
a = float(input('Digite um ângulo: '))
print(f'O ângulo de {a:.2f}º possui:\n'
      f'Seno: {sin(radians(a)):.2f}\n'
      f'Cosseno: {cos(radians(a)):.2f}\n'
      f'Tangente: {tan(radians(a)):.2f}')

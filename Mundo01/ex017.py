# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot
catetoOp = float(input('Digite o valor do cateto oposto: '))
catetoAd = float(input('Digite o valor do cateto adjacente: '))
print(f'O valor da hipotenusa é {hypot(catetoOp, catetoAd):.2f}')

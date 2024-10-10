# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
numero = input("Digite um número de 0 a 9999: ")
numero_str = numero.zfill(4)
print(f"Milhar: {numero_str[0]}")
print(f"Centena: {numero_str[1]}")
print(f"Dezena: {numero_str[2]}")
print(f"Unidade: {numero_str[3]}")

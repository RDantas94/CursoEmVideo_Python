# Faça um programa que leia três números e mostre qual é o maior e qual é o menor
n1 = float(input('Digite um número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o último número: '))
maior = max(n1, n2, n3)
menor = min(n1, n2, n3)
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")

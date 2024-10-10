# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR
numero = int(input("Digite um número: "))
if numero == 0:
    print("O número 0 é neutro. Por favor, insira um número diferente de 0.")
elif numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")
print('Fim do programa!')

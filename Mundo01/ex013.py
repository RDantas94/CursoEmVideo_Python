# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento
salario = float(input('Digite o salário atual: R$'))
aumento = (salario*15)/100
novoSalario = salario + aumento
print(
    f'o salário R${salario:.2f}, após aumento de R${aumento}(15%), passará a ser de R${novoSalario:.2f}')

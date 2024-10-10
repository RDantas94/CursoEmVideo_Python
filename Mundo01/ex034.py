# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250.00, calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%
sal = float(input('Digite seu salário: R$'))
if sal <= 1250.00:
    novosal = sal+(sal*15/100)
    aum = 15
else:
    novosal = sal+(sal*10/100)
    aum = 10
print(
    f'Seu salário era de R${sal:.2f} e com um aumento de {aum}% passou a ser de R${novosal:.2f}')

# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
preco_casa = float(input('Digite o valor da casa: R$'))
anos = int(input('Em quantos anos deseja pagar? '))
salario = float(input('Digite seu salário:: R$'))

prestacao = preco_casa/(anos * 12)
limite = salario * 30 / 100

print(f'Para pagar uma casa de R${preco_casa:.2f} em {
      anos}, a prestação será de R${prestacao}')
if prestacao >= limite:
    print('Sua prestação excedeu seu limite. Seu empréstimo foi negado, sinto muito!')
else:
    print('Parabéns, seu empréstimo foi aprovado!')

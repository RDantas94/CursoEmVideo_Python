# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
preco = float(input('Digite o preço do produto: R$'))
desconto = (preco*5)/100
novoPreco = preco - desconto
print(
    f'O produto que custava R${preco:.2f}, após o desconto de 5% passará a custar R${novoPreco:.2f}')

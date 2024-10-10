# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0.50 por Km para viagens de até 200Km e R$0.45 para viagens mais longas
dist = float(input('Digite a distância até o destino em Km: '))
if dist <= 200:
    preco = dist*0.50
    print(
        f'O valor total de sua viagem de {dist}Km foi de R${preco:.2f}, cobrando R$0.50 por Km')
else:
    preco = dist*0.45
    print(
        f'O valor total de sua viagem de {dist}Km foi de R${preco:.2f}, cobrando R$0.45 por Km')
print('Fim do programa!')

# Escreva um programa que leia a velocidade de um carro. se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado
# A multa vai custar R$7.00 por cada Km acima do limite
vel = float(input('Digite a velocidade do carro em Km/h: '))
if vel > 80:
    multa = (vel - 80) * 7
    print(
        f'Você excedeu o limite permitido da via(80Km/h) foi multado! \nO valor da multa é de R${multa:.2f}')
print('Dirija com segurança!')

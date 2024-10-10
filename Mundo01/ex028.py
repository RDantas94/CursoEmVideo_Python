# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep
num = randint(0, 5)  # Gera um número no intervalo entre 0 e 5
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-'*20)
usu = int(input('Escolha um número de 0 a 5: '))
print('PROCESSANDO...')
sleep(3)
if num == usu:
    print(f'Você acertou! O número escolhido era {num}')
else:
    print(f'Que pena, o número certo era {num}')
print('Obrigado por jogar!')

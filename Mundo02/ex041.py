# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
'''
- até 9 anos: Mirim
- até 14 anos: Infantil
- até 19 anos: Junior
- até 25 anos: Sênior
- acima: Master
'''
from datetime import date
atual = date.today().year
nasc = int(input('Em que ano você nasceu? '))
idade = atual - nasc
if idade <= 9:
    print('MIRIM')
elif 10 <= idade <= 14:
    print('INFANTIL')
elif 15 <= idade <= 19:
    print('JUNIOR')
elif idade == 20:
    print('SENIOR')
else:
    print('MASTER')

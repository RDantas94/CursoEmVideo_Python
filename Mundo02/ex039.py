# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
atual = date.today().year
nasc = int(input('Em que ano você nasceu? '))
alis = 18
idade = atual - nasc
if idade < alis:
    anos_faltam = alis - idade
    print(f"Você ainda vai se alistar ao serviço militar. Faltam {
          anos_faltam} ano(s) para o alistamento.")
elif idade == alis:
    print("É hora de se alistar ao serviço militar.")
else:
    anos_passaram = idade - alis
    print(f"Você já passou do tempo de alistamento. Passaram {
          anos_passaram} ano(s) do prazo.")

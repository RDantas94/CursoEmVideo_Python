# Calculo do IMC
peso = float(input('Digite seu peso em Kg: '))
alt = float(input('Digite sua altura em Metros: '))
imc = peso/(alt**2)

print(f'Seu IMC é de {imc:.1f} e você: ', end='')
if imc < 18.5:
    print('Está Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Está no Peso ideal')
elif 25 <= imc < 30:
    print('Está em Sobrepeso')
elif 30 <= imc < 40:
    print('Está em Obesidade')
else:
    print('Está em Obesidade mórbida')

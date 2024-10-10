# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
# Atualização: Exibir o restante de unidades de medidas

# Leitura do valor em metros
m = float(input('Digite o valor em metros para conversão: '))

# Conversões para diferentes unidades
km = m / 1000         # Quilômetros
hm = m / 100          # Hectômetros
dam = m / 10          # Decâmetros
dm = m * 10           # Decímetros
cm = m * 100          # Centímetros
mm = m * 1000         # Milímetros

# Exibindo os resultados das conversões
print(f'O valor de {m}m equivale a:')
print(f'{km} km (quilômetros)')
print(f'{hm} hm (hectômetros)')
print(f'{dam} dam (decâmetros)')
print(f'{dm:.0f} dm (decímetros)')
print(f'{cm:.0f} cm (centímetros)')
print(f'{mm:.0f} mm (milímetros)')

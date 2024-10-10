# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# Considere US$1.00 = R$3.27 (;-;)
r = float(input('Digite quantos reais você tem: R$'))
d = r/3.27
print(f'Após conversão, você terá US${d:.2f}')

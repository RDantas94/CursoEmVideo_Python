# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.
distancia = float(input('KMs percorridos pelo carro alugado:'))
dias = int(input('Dias alugado: '))
total = (dias*60)+(distancia*0.15)
print(f'Total a ser pago R${total:.2f}, dos quais\n'
      f'R${distancia*0.15:.2f} equivalem a distância percorrida e \n'
      f'R${dias*60:.2f} aos dias alugados.')

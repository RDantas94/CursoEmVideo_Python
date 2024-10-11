# Refaça o desafio 035(ex035 do mundo01) dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
'''
- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
'''
reta1 = float(input("Digite o comprimento da primeira reta: "))
reta2 = float(input("Digite o comprimento da segunda reta: "))
reta3 = float(input("Digite o comprimento da terceira reta: "))
if (reta1 + reta2 > reta3) and (reta1 + reta3 > reta2) and (reta2 + reta3 > reta1):
    print("As retas podem formar um triângulo ", end="")
    if reta1 == reta2 == reta3:
        print("Equilátero: todos os lados iguais.")
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print("Isósceles: dois lados iguais.")
    else:
        print("Escaleno: todos os lados diferentes.")
else:
    print("As retas não podem formar um triângulo.")

# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversâo:
''' 1 para binário
    2 para octal
    3 para hexadecimal'''


def converter_numero():
    '''Converte um número inteiro na base númerica escolhida
    Input:
    - numero

    Output:
    - numero convertido com a base escolhida

    '''
    numero = int(input("Digite um número inteiro: "))
    print("Escolha a base de conversão:")
    print("1 para Binário")
    print("2 para Octal")
    print("3 para Hexadecimal")
    escolha = int(input("Sua escolha: "))
    if escolha == 1:
        print(f"O número {numero} em binário é: {bin(numero)[2:]}")
    elif escolha == 2:
        print(f"O número {numero} em octal é: {oct(numero)[2:]}")
    elif escolha == 3:
        print(f"O número {numero} em hexadecimal é: {hex(numero)[2:]}")
    else:
        print("Escolha inválida!")


converter_numero()

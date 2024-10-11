from time import sleep
import os


def exibir_titulo():
    print('''
▒█░░░ █▀▀█ ░░▀ █▀▀█ █▀▀ 　 ▒█▀▀▀ ▒█▀▀█ 
▒█░░░ █░░█ ░░█ █▄▄█ ▀▀█ 　 ▒█▀▀▀ ▒█▄▄█ 
▒█▄▄█ ▀▀▀▀ █▄█ ▀░░▀ ▀▀▀ 　 ▒█░░░ ▒█░░░
          ''')


def carregando(t):
    print('CARREGANDO...')
    sleep(t)
    os.system('cls')


def menu_principal():
    print('Selecione a forma de pagamento:')
    print("1 - Dinheiro ou Pix (10% de desconto)")
    print("2 - Cartão débito/crédito à vista (5% de desconto)")
    print("3 - Cartão crédito parcelado")


def opcao_invalida():
    print('Opção inválida, retorne ao menu inicial!')
    voltar_ao_menu_principal()


def voltar_ao_menu_principal():
    input('Digite uma tecla para voltar ao menu: ')
    main()


def calcular_total(preco, desconto_ou_juros):
    """
    Aplica desconto (valor negativo) ou juros (valor positivo) sobre o preço.
    """
    return preco * (1 + desconto_ou_juros / 100)


def exibir_valor(preco_inicial, total, metodo_pagamento, parcelas=1):
    """
    Exibe o valor inicial, o método de pagamento, o total e, opcionalmente, o valor das parcelas.
    """
    print(f"Valor inicial do produto: R${preco_inicial:.2f}")
    print(f"Método de pagamento: {metodo_pagamento}")

    if parcelas > 1:
        valor_parcela = total / parcelas
        print(f'O total a ser pago é R${total:.2f}, dividido em {
              parcelas} parcelas de R${valor_parcela:.2f}')
    else:
        print(f'O total a ser pago é R${total:.2f}')


def pagamento_a_vista(preco, desconto, metodo_pagamento):
    total = calcular_total(preco, -desconto)
    exibir_valor(preco, total, metodo_pagamento)


def cartao_parcelado(preco):
    print('Deseja parcelar em duas ou três vezes?')
    print('1 - Parcelar em 2 vezes (sem juros)')
    print('2 - Parcelar em 3 ou mais vezes (20% de juros)')
    opcao2 = int(input('Opção selecionada: '))

    carregando(2)

    match opcao2:
        case 1:
            exibir_valor(preco, preco, "Cartão em 2 vezes", 2)
        case 2:
            total = calcular_total(preco, 20)  # Aplica 20% de juros
            parcelas = int(input('Insira o número de parcelas (mínimo 3): '))
            if parcelas >= 3:
                exibir_valor(
                    preco, total, "Cartão em 3 ou mais vezes", parcelas)
            else:
                opcao_invalida()
        case _:
            opcao_invalida()


def escolher_opcao(preco):
    try:
        opcao = int(input('Opção selecionada: '))
        carregando(2)
        match opcao:
            case 1:
                pagamento_a_vista(
                    preco, 10, "Dinheiro ou Pix (10% de desconto)")
            case 2:
                pagamento_a_vista(preco, 5, "Cartão à vista (5% de desconto)")
            case 3:
                cartao_parcelado(preco)
            case _:
                opcao_invalida()
    except ValueError:
        opcao_invalida()


def main():
    os.system('cls')
    exibir_titulo()
    preco = float(input('Digite o valor do produto: R$'))
    menu_principal()
    escolher_opcao(preco)


main()

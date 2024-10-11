from random import randint

# Lista de opções
opcoes = ["Pedra", "Papel", "Tesoura"]


def titulo():
    jokenpo = '''🅹🅾 🅺 🅴 🅽🅿 🅾'''
    linha = '*' * len(jokenpo)
    print(linha)
    print(jokenpo)
    print(linha)


def mostrar_opcoes():
    """Mostra as opções disponíveis para o jogador."""
    print('Escolha sua jogada:')
    print('0 - Pedra')
    print('1 - Papel')
    print('2 - Tesoura')


def escolher_jogada():
    """Solicita e retorna a jogada do usuário."""
    try:
        jogada = int(input('Digite o número da sua escolha: '))
        if jogada < 0 or jogada > 2:
            print('Escolha inválida! Tente novamente.')
            return escolher_jogada()  # Rechama a função em caso de escolha inválida
        return jogada
    except ValueError:
        print('Entrada inválida! Digite um número entre 0 e 2.')
        return escolher_jogada()  # Rechama a função em caso de erro


def jogada_computador():
    """Retorna a jogada do computador (aleatória)."""
    return randint(0, 2)


def verificar_vencedor(usu, oponente):
    """Verifica o vencedor do jogo e retorna o resultado."""
    if usu == oponente:
        return 'Empate'
    elif (usu == 0 and oponente == 2) or (usu == 1 and oponente == 0) or (usu == 2 and oponente == 1):
        return 'Jogador'
    else:
        return 'Computador'


def jogar_novamente():
    """Pergunta ao usuário se ele deseja jogar novamente."""
    resposta = input("Gostaria de jogar novamente? (S/N): ").strip().upper()
    if resposta == 'S':
        return True
    elif resposta == 'N':
        return False
    else:
        print('Opção inválida. Digite "S" para Sim ou "N" para Não.')
        return jogar_novamente()  # Rechama a função se a resposta for inválida


def main():
    while True:
        mostrar_opcoes()
        usu = escolher_jogada()
        oponente = jogada_computador()

        print(f'Você escolheu: {opcoes[usu]}')
        print(f'O computador escolheu: {opcoes[oponente]}')

        resultado = verificar_vencedor(usu, oponente)

        if resultado == 'Empate':
            print('Empate! Vamos jogar novamente até ter um vencedor.')
        else:
            print(f'{resultado} venceu!')
            if not jogar_novamente():
                print('Obrigado por jogar! Até a próxima.')
                break


# Inicia o jogo
main()

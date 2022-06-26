import sys


def leiaInt(msg):
    while True:
        try:
            inteiro = int(input(msg))

        except (ValueError, TypeError):
            print('\033[31m Erro: por favor digite um número inteiro válido. \033[m')
        except KeyboardInterrupt:
            print('\n \033[31m Entrada de dados interrompida pelo usuário \033[m')
            sys.exit(0)

        else:
            return inteiro


def leiaFloat(msg):

    while True:
        try:
            real = str(input(msg)).strip().replace(',', '.')
            real = float(real)
        except (ValueError, TypeError):
            print('\033[31m Erro: Por favor, digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print('\n \033[31m Entrada de dados interrompida pelo usuário \033[m')
            sys.exit(0)

        else:
            return real







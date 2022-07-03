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


def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):

    cabeçalho('MENU PRINCIPAL')
    c = 1
    for d in lista:
        print(f'\033[33m{c}\033[m - \033[34m{d}\033[m')
        c += 1
    print(linha())
    resposta = leiaInt('Sua Opção: ')
    return resposta

def ajuda(com):
    from time import sleep
    titulo('Acessando o manual do comando ' + com, cores['azul'])
    sleep(2)
    print(cores['branco'])
    help(com)
    print(cores['limpa'],end='')
    sleep(6)


def titulo(msg, cor):
    tam = len(msg.strip()) + 4
    print(cor, end='')
    print('~' * tam)
    print(msg)
    print('~' * tam)
    print(cores['limpa'], end='')


# Programa Principal


cores = {
    'verde': '\033[97;42m',
    'vermelho': '\033[97;41m',
    'azul': '\033[97;44m',
    'branco': '\033[30;107m',
    'limpa': '\033[m'
}

while True:
    titulo('  SISTEMA DE AJUDA PyHELP  ', cores['verde'])
    com = str(input('Função ou Biblioteca > (fim para terminar) ')).lower()
    if com == 'fim':
        titulo('  ATÉ LOGO!  ', cores['vermelho'])
        break
    ajuda(com)

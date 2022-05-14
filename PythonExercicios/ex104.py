def leiaInt(txt):
    cor = {'inicio': '\033[1:31m', 'fim': '\033[m'}
    while True:
        num = str(input(txt))
        if num.isnumeric():
            break
        print(f'{cor["inicio"]}ERRO! Digite um número válido.{cor["fim"]}')

    return int(num)


# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')

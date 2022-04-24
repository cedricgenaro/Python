from time import sleep


def linha():
    print('-='*20)


def contador(i, f, p):
    linha()
    print(f'Contagem de {i} até {f} de {p.__abs__()} em {p.__abs__()}')
    if i > f:
        f -= 1
        if p > 0:
            p *= -1
    else:
        f += 1
    for c in range(i, f, p):
        print(f'{c} ', end='')
        sleep(0.4)
    print('FIM!')


#PROGRAMA PRINCIPAL

contador(1, 10, 1)
contador(10, 0, -2)
linha()
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
if passo == 0:
    passo = 1
    print('Passo 0 considerando passo 1')
contador(inicio, fim, passo)

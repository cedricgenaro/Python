def fatorial(n, show=False):
    """
    -> Função que calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    fatorial = 1
    for c in range(n, 0, -1):
        fatorial *= c
        if show:
            print(f'{c} ', end='')
            if c > 1:
                print('x ', end='')
            else:
                print('= ', end='')

    return fatorial


print('-'*25)
print(fatorial(5))


def aumentar(preco=0.00, taxa=0):
    res = preco + (preco * (taxa / 100))
    return res


def diminuir(preco=0.00, taxa=0):
    res = preco - (preco * (taxa / 100))
    return res


def dobro(preco=0.00):
    res = preco * 2
    return res


def metade(preco=0.00):
    res = preco / 2
    return res


def moeda(preco=0.00, moeda='R$'):
    res = str(f'{moeda} {preco:2.2f}').replace('.', ',')
    return res

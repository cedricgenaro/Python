def aumentar(preco=0.00, taxa=0, format=False):
    res = preco + (preco * (taxa / 100))
    return res if format is False else moeda(preco)


def diminuir(preco=0.00, taxa=0, formato=False):
    res = preco - (preco * (taxa / 100))
    return res if formato is False else moeda(res)


def dobro(preco=0.00, formato=False):
    res = preco * 2
    return res if not formato else moeda(res)


def metade(preco=0.00, formato=False):
    res = preco / 2
    return res if formato is False else moeda(res)


def moeda(preco=0.00, moeda='R$'):
    res = str(f'{moeda} {preco:2.2f}').replace('.', ',')
    return res

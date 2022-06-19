def aumentar(preco=0.00, taxa=0, formato=False):
    res = preco + (preco * (taxa / 100))
    return res if formato is False else moeda(res)


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


def resumo(preco=0.00, aumento=10, desconto=5):
    print('-'*40)
    print('RESUMO DO VALOR'.center(40))
    print('-' * 40)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{aumento:<3}% de aumento: \t{aumentar(preco, aumento, True)}')
    print(f'{desconto:<3}% de redução: \t{diminuir(preco, desconto, True)}')
    print('-' * 40)

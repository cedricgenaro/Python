opção = produtobarato = ''
barato = total = maisde1000 = 0

print('---'*15)
print(f'{"LOJA SUPERLAR BARATÃO":^40}')
print('---'*15)
while True:
    produto = str(input('Nome do Produto: ')).strip()
    preço = float(input('Preço: R$'))
    if barato == 0 and produtobarato == '':
        barato = preço
        produtobarato = produto
    else:
        if preço < barato:
            barato = preço
            produtobarato = produto
    total += preço
    if preço > 1000:
        maisde1000 += 1
    opção = str(input('Quer contnuar? [S/N] ')).strip().upper()[0]
    while opção not in 'NS':
        opção = str(input('Dado inválido! Quer continuar? [S/N] ')).strip().upper()[0]

    if opção == 'N':
        break
print(f'{" FIM DO PROGRAMA ":-^40}')
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {maisde1000} produtos custando mais de R$1000.00' if maisde1000 > 1 else f'Temos {maisde1000} produto custando mais de R$1000.00')
print(f'O produto mais barato foi {produtobarato} custando R${barato:.2f}')


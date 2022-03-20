print('\n {:=^50}'.format(' Preço final com 5% de desconto '))
preco = float(input('\n Digite o preço do produto: R$ '))
desconto = (5 / 100) * preco
print('-'*100)
print('Preço final: R${:.>10.2f}'.format(preco - desconto))




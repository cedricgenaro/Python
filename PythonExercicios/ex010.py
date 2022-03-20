print('{:=^50}'.format('Dólares'))
cart = float(input('\n Digite quanto dinheiro tem na carteira? R$'))
dolar = cart / 5.21
print('-'*50)
print('Com R${:.2f} você pode comprar: US${:.2f} '.format(cart, dolar))

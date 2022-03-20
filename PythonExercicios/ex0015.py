print('{:=^50}'.format(' ALUGUEL DE CARRO '))
dias = int(input('Quantos dias ele foi usado? '))
km = float(input('Quantos Km foram percorridos? '))

valorfinal = (80 * dias) + (km * 0.15)
print('-'*60)
print('Um veículo usado por {} dias que percorreu {}Km, terá que pagar: R${:.2f} '.format(dias, km, valorfinal))

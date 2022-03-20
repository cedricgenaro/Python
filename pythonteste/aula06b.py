n = input('Digite algo: ')
print('Qual é o seu tipo? {}'.format(type(n)))
print('É um número? {}'.format(n.isnumeric()))
print('São letras? {}'.format(n.isalpha()))
print('Tem letras ou números? {}'.format(n.isalnum()))
print('Todas as letras são maiúsculas? {}'.format(n.isupper()))


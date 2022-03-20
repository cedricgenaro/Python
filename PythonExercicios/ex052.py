divisivel = 0
print('{:^25}'.format('É PRIMO?'))
print('---'*20)
numero = int(input('Digite um número: ').strip())
for cont in range(1, numero+1):
    if numero % cont == 0:
        print(f'\033[1;36m {cont}\033[m', end=' ')
        divisivel += 1
    else:
        print(f'\033[0;33m {cont}\033[m', end=' ')
print('\nO número {} foi divisível {} vezes'.format(numero, divisivel))
if divisivel > 2:
    print('E por isso ele NÃO É PRIMO'.format(numero))
else:
    print('E por isso ele É PRIMO!'.format(numero))

print('-=-'*60)
print('É par ou ímpar')
print('-=-'*60)
n = int(input('Me diga um número qualquer: '))
res = 'PAR' if n % 2 == 0 else 'ÍMPAR'
print('O número {} é {}'.format(n, res))

número = int(input('Me diga um número qualquer: '))
resultado = número % 2
if resultado == 0:
    print('O número {} é PAR'.format(número))
else:
    print('O número {} é ÍMPAR'.format(número))

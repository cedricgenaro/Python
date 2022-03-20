print('\033[34m-=-'*15)
print('analisador de triângulos '.upper())
print('-=-'*15)
pseg = float(input('\033[mPrimeiro segmento: ').strip())
sseg = float(input('Segundo segmento: ').strip())
tseg = float(input('Terceiro segmento: ').strip())
if pseg + sseg > tseg:
    res = 'podem formar'.upper()
    cor = '\033[1;32m'
else:
    res = 'não podem formar'.upper()
    cor = '\033[1;31m'
print('Os segmentos acima {}{}{} triângulo'.format(cor, res, '\033[m'))

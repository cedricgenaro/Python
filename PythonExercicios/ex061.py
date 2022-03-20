# decimo = primeiro + (10 - 1).razao
cont = 1
pa = 0
print('Gerador de PA')
print('-=-'*15)

primeiroTermo = int(input('Primeiro termo: ').strip())
razão = int(input('Razão da PA: ').strip())
pa = primeiroTermo
while cont <= 10:
    print(pa, end=' → ')
    pa += razão
    cont += 1
print('FIM')





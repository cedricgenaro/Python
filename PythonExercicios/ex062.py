#Super progressão aritimética
cont = 1
termos = 10
pa = 0
somatermos = termos
print('{:=^30}'.format(' Gerador de PA '))
ptermo = int(input('Primeiro termo: '))
pa = ptermo
razao = int(input('Razão: '))
while termos != 0:
    while cont <= termos:
        print('{} → '.format(pa), end='')
        pa += razao
        cont += 1
    print('PAUSA')
    cont = 1
    termos = int(input('Quantos termos você quer mostrar mais? '))
    somatermos += termos
print('Progressão Finalizada com {} termos mostrados.'.format(somatermos))

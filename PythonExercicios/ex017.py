'''
Primeira solução

from math import sqrt
catop = float(input('Comprimento do cateto oposto: '))
catadj = float(input('Comprimento do cateto adjacente: '))
hip = sqrt(pow(catop, 2) + pow(catadj, 2))
print('A hipotenusa vai medir {:.2f}'.format(hip))'''

'''Segunda solução'''

from math import hypot

catop = float(input('Comprimento do Cateto oposto: '))
catadj = float(input('Comprimento do Cateto adjacente: '))
print('A hipotenusa vai medir: {:.2f}'.format(hypot(catadj, catop)))




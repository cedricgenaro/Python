'''CALCULO DO SENO, COSSENO E TANGENTE '''
from math import sin, cos, tan, radians
ang = float(input('Digite o ãngulo que você deseja: '))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ang, sin(radians(ang))))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ang, cos(radians(ang))))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ang, tan(radians(ang))))






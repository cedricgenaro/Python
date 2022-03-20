from os import system

import os
n = s = 0
while True:
    os.system("cls")
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
    #print('\n'*130)

# print('A soma vale {}'.format(s))
print(f'A soma vale {s}')





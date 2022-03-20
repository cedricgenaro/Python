# seqfinacci = 0
# antecessor = 0
# cont = 1
# print('--'*20)
# print('Sequência de Fibonacci')
# print('--'*20)
# n = int(input('Quantos termos você quer mostrar? '))
# print('~~'*20)
# while cont <= n:
#
#     print('{} → '.format(seqfinacci), end='')
#     if seqfinacci < 1:
#         seqfinacci = 1
#     else:
#         seqfinacci = seqfinacci  + antecessor
#         antecessor = seqfinacci - antecessor
#     cont += 1
# print('FIM')
# print('~~'*20)
n = int(input('Quantos termos você quer ver? '))
t1 = 0
t2 = 1
print('{} → {} '.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t2 + t1
    print(' → {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1


# progressao = 0
# print('=='*20)
# print('{:^40}'.format('10 TERMOS DE UMA PA'))
# print('=='*20)
# progressao = int(input('Primeiro termo: ').strip())
# razão = int(input('Razão: ').strip())
# for cont in range(0, 10):
#     print('{} \u27F6 '.format(progressao), end='')
#     progressao += razão
# print('ACABOU!')

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print('{} '. format(c), end='→ ')
print('ACABOU')


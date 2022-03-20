print('{:-^50}'.format('tabuada'.upper()))
número = int(input('Digite um número para ver a sua tabuada: ').strip())
print('-'*50)
for num in range(0, 11):
    print('{} X {} = {}'.format(número, num, número * num))


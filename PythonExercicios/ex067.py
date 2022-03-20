while True:
    num = int(input('Quer ver a tabuada de qual valor?: '))
    print('---' * 15)
    if num < 0:
        break
    for i in range(1, 11):
        print(f'{num} x {i} = {num * i}')
    print('---'*15)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')

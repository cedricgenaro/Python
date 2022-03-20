numeros = 0
paresimpares = [[], []]
for i in range(0, 7):
    numeros = int(input(f'Digite o {i+1}º valor: '))
    if numeros % 2 == 0:
        paresimpares[0].append(numeros)
    else:
        paresimpares[1].append(numeros)
paresimpares[0].sort()
paresimpares[1].sort()
print('-='*35)
print(f'Os valores pares digitados foram: {paresimpares[0]}')
print(f'Os valores ímpares digitados foram: {paresimpares[1]}')



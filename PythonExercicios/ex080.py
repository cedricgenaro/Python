valores = list()
valor = 0
for c in range(0, 5):
    valor = int(input('Digite um valor: '))
    if c == 0 or valor >= valores[len(valores)-1]:
        valores.append(valor)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(valores):
            if valor <= valores[pos]:
                valores.insert(pos, valor)
                print(f'Adicionado na posição {pos}..')
                break
            pos += 1

print('-='*30)
print(f'Os valores digitados em ordem foram {valores}')


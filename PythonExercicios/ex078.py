
valores = []
maior = menor = 0
for i in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {i}: ')))
    if i == 0:
        maior = menor = valores[i]
    elif valores[i] >= maior:
        maior = valores[i]
    elif valores[i] <= menor:
        menor = valores[i]
print('=-'*35)
print(f'Você digitou os valores {valores}')
print(f'O Maior valor digitado foi {maior} nas posições ', end='')
for p, v in enumerate(valores):
    if v == maior:
        print(p, end='... ')
print(f'\nO menor valor valor digitado foi {menor} nas posições ', end='')
for p, v in enumerate(valores):
    if v == menor:
        print(p, end='... ')


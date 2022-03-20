cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
        'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
     while True:
        numero = int(input('Digite um número entre 0 e 20: '))
        if 0 <= numero <= 20:
         break
        print('Tente novamente! ', end='')
     print(f'Você digitou o número \033[1m{cont[numero]}')
     print('---'*15)
     opcao = ' '
     while opcao not in 'SN':
         opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
     if opcao == 'N':
        break
     print('Tente novamente! ', end='')


print('Obrigado volte sempre!')



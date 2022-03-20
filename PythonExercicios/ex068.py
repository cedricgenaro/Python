from random import randint
total = vitoria = 0
print('-=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=-'*15)
while True:
    num = int(input('Diga um valor: '))
    numcomp = randint(1, 10)
    while True:
        escolha = str(input('Par ou Ímpar [P/I] ').strip())[0].upper()
        if escolha not in 'iIpP':
            print('Opção inválida! Tente novamente')
        else:
            break
    total = num + numcomp
    print('---'*15)
    if escolha == 'P':
        if total % 2 == 0:
            vitoria += 1
            print(f'Você jogou {num} e o computador {numcomp}. Total de {total} DEU PAR')
            print('---' * 15)
            print('Você VENCEU!')

        else:
            print(f'Você jogou {num} e o computador {numcomp}. Total de {total} DEU ÍMPAR')
            print('---' * 15)
            print('Você PERDEU!')
            print('-=-' * 15)
            break
    if escolha == 'I':
        if total % 2 != 0:
            vitoria += 1
            print(f'Você jogou {num} e o computador {numcomp}. Total de {total} DEU ÍMPAR')
            print('---' * 15)
            print('Você VENCEU!')
        else:
            print(f'Você jogou {num} e o computador {numcomp}. Total de {total} DEU PAR')
            print('---' * 15)
            print('Você PERDEU!')
            print('-=-'*15)
            break
    print('Vamos jogar novamente...')
    print('-=-' * 15)
print(f'GAME OVER! você venceu {vitoria} vezes.')

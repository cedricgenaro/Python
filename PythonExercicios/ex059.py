from time import sleep
opcao = 0
soma = 0
multiplicar = 0
n1 = int(input('Primeiro valor: ').strip())
n2 = int(input('Segundo Valor: ').strip())
maior = n1
while opcao != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior 
    [ 4 ] Digitar novos números
    [ 5 ] Sair do programa ''')
    opcao = int(input('>>>>> Qual é a sua opção? ').strip())
    if opcao == 1:
        soma = n1 + n2
        print('A soma de {} + {} = {}'.format(n1, n2, soma))
    if opcao == 2:
        multiplicar = n1 * n2
        print('A Multiplicação de {} x {} = {}'.format(n1, n2, multiplicar))
    if opcao == 3:
        if maior < n2:
            maior = n2
        print('Entre {} e {} o maior é {}'.format(n1, n2, maior))
    if opcao == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: ').strip())
        n2 = int(input('Segundo valor: ').strip())
        maior = n1
    if opcao > 5:
        print('Opção inválida. Tente novamente')
    print('=-='*15)
    sleep(3)
print('Fim do programa! Obrigado e volte sempre')





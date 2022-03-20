print('--'*50)
print('{:^50}'.format('CONVERSOR DE BASES'))
print('--'*50)
número = int(input('DIGITE UM NÚMERO INTEIRO QUALQUER: '))
print('''
    OPÇÕES PARA CONVERSÃO:
    [1] BINÁRIO
    [2] OCTAL
    [3] HEXADECIMAL
       ''')
opção = int(input('DIGITE O NÚMERO DA SUA OPÇÃO: '))
print('--'*50)
if opção == 1:
     print('BINÁRIO: {0:b}'.format(número))
elif opção == 2:
    print('OCTAL: {:o}'.format(número))
elif opção == 3:
    print('HEXADECIMAL: {:X}'.format(número))
else:
    print('OPÇÃO INVÁLIDA TENTE NOVAMENTE!')



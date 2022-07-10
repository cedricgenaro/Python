nome = str(input('Digite seu nome completo: '))


with open('bancodados/teste.txt', 'a') as f:
    f.write(nome + '\n')
with open('bancodados/teste.txt', 'r') as f:
    print(f.readlines())

if f:
    print('Arquivo existe')

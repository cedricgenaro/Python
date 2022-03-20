# numero = int(input('Digite um número [999 para parar]: ').strip())
# soma = numero
# cont = 1
# while numero != 999:
#     numero = int(input('Digite um número [999 para parar]: ').strip())
#     if numero != 999:
#         soma += numero
#         cont += 1
# print('Você digitou {} números e a soma entre eles foi {}'.format(cont, soma))

num = cont = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} e a soma entre eles foi {}'.format(cont, soma))


# PROGRAMA EMPRÉSTIMO
print('\033[1;36m---'*50)
print('{:^80}'.format('CONCESSÃO DE EMPRÉSTIMO'))
print('---'*50+'\033[m')
casa = float(input('qual o valor da casa? r$'.upper()).strip())
salário = float(input('qual o valor do seu salário? r$'.upper()).strip())
anos = int(input('quantos anos de financiamento? '.upper()).strip())
prestacao = (casa / anos) / 12
limite = salário * (30/100)
print('\033[1;36m'+'---'*50+'\033[m')
print('{} PARA PAGAR UMA CASA DE R${:.2f} EM {} ANOS A PRESTAÇÃO SERÁ DE R${:.2f}{}'.format('\033[1;36m', casa, anos, prestacao,'\033[m'))
print('\033[1;36m'+'---'*50+'\033[m')
if prestacao >= limite:
    print('\033[1;31m EMPRÉSTIMO NÃO CONCEDIDO!\033[m')
else:
    print('\033[1;32m EMPRÉSTIMO CONCEDIDO!\033[m')





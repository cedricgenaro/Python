from lib.interface import *
from time import sleep
from os import system

cabeçalho('SISTEMA ARQUIVO v.1.0')
while True:
    system('cls')
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoas', 'Sair do Sistema'])
    if resposta == 1:
        cabeçalho('Opção 1')

    elif resposta == 2:
        cabeçalho('Opção 2')

    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        sleep(2)
        break
    else:
        print('\033[31mERRO: por favor digite uma opção válida!\033[m')
    sleep(2)

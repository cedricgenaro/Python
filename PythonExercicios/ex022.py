'''Minha solução

nomec = str(input('Digite seu nome completo: '))
letrasnomec = len(''.join(nomec.split()))
primeironome = nomec.split()

print("Analisando seu nome...\n"
      "Seu nome em maiúsculas é {} \n"
      "Seu nome em minúsculas é {} \n"
      "Seu nome tem ao todo {} letras \n"
      "seu primeiro nome é {} e ele tem {} letras".format(nomec.upper(), nomec.lower(), letrasnomec, primeironome[0].title(), len(primeironome[0])))
'''

'''SOLUÇÃO DO PROFESSOR'''
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome..')
print('Seu nome em maúsculas é {}'.format(nome.upper()))
print('seu nome em minúsculas é {}'.format(nome.lower()))
print('seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} tem {} letras'.format(separa[0], len(separa[0])))






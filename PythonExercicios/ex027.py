nome = str(input('Digite seu nome completo: ')).strip()
nomesep = nome.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nomesep[0].title()))
print('Seu ultimo nome é {}'.format(nomesep[len(nomesep)-1].title()))



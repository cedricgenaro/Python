'''Minha solução'''
'''import random
aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')

alunoescolhido = random.choice([aluno1, aluno2, aluno3, aluno4])
print('O aluno escolhido foi {}'.format(alunoescolhido))'''

'''Solução do Professor'''
import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi: {}'.format(escolhido))


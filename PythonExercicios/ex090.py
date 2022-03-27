aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if 7 >= aluno['Média'] >= 5:
    aluno['Situação'] = 'Recuperação'
elif aluno['Média'] > 7:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'
print('-='*20)
for k, v in aluno.items():
    print(f'- {k} é igual a {v}')


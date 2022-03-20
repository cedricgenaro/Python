from time import sleep
bd = []
op = 0
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    bd.append([nome, [nota1, nota2], media])
    op = str(input('Quer continuar? [S/N] '))
    if op in 'nN':
        break
print('-='*50)
print(f'Nº{"Nome":>6}{"MÉDIA":>18}')
print('-'*35)
for i, dado in enumerate(bd):
    print(f'{i:<4}{dado[0]:<18}{dado[2]}')
print('-='*80)
while True:
    op = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if op == 999:
        break
    if op <= len(bd):
        print(f'Notas de {bd[op][0]} são {bd[op][1]}')
    sleep(3)

print('FINALIZANDO...')
sleep(5)
print('<<< VOLTE SEMPRE >>>')



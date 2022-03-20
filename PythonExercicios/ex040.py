print('--'*40)
print('{:^70}'.format('\033[1m ESCOLA CARROSSEL \033[m'))
print('--'*40)
nt1 = float(input('Digite sua primeira nota: ').strip())
nt2 = float(input('Digte sua segunda nota: ').strip())
print('--'*40)
media = (nt1 + nt2) / 2
print('Tirando {} e {}, a média do aluno é {:.1f}'.format(nt1, nt2, media))
if media < 5:
    print('O aluno está \033[1;97;41m REPROVADO! \033[m')
elif media < 7:
    print('O aluno está de \033[1;97;43m RECUPERAÇÃO! \033[m')
else:
    print('O aluno está \033[1;97;42m APROVADO! \033[m')

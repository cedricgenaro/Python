itens = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
         'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-'*42)
print(f'{"LISTAGEM DE PREÇOS":^42}')
print('-'*42)
for it in range(0, len(itens)-1):
    if it % 2 == 0:
        print(f'{itens[it]:.<30}', f'R${itens[it+1]:>8.2f}')
print('-'*42)

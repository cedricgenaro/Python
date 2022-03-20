palavra = ('Passaro', 'Ceu', 'Estrela', 'Planeta', 'cometa', 'barco', 'pessoa', 'Camisa', 'piranha', 'triangulo')
for pal in palavra:
    print(f'\n Na palavra {pal.upper()} suas vogais são:', end=' ')
    for c in range(0, len(pal)):
        if pal[c].lower() in 'aeiou':
            print(pal[c].lower(), end=' ')






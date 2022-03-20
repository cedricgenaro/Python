times = ('Atlético Mineiro', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Red Bull Bragantino', 'Fluminense',
    'America', 'Atlético', 'Santos', 'Ceará ', 'Internacional', 'São Paulo', 'Athletico Paranaense', 'Cuiabá', 'Juventude',
    'Grêmio', 'Bahia ', 'Sport', 'Chapecoense')

print('-=-'*15)
print(f'Lista de times do Brasileirão: \033[1m {times}')
print('-=-'*15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=-'*15)
print(f'Os 4 últimos são {times[-4:]}')
print('-=-'*15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=-'*15)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição')

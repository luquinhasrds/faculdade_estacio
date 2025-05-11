from random import randint
from time import sleep
from operator import itemgetter
i = 1

jogadores= dict()

for i in range(4):
    jogador = f'Jogador {i+1}'
    jogadores[jogador] = randint(1, 6)
    sleep(1)
    print(f'O {jogador} tirou {jogadores[jogador]}')
    
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print('-'*40)
for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]} pontos.')
print('-'*40)

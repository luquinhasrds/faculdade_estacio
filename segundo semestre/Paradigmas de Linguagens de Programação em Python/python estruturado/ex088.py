from random import randint
num = 1

quant = int(input('Digite a quantidade de jogos que voce quer fazer: '))

jogos = [[randint(1, 60) for _ in range(6)] for _ in range(quant)]


for lista in jogos:
    print(f'Jogo {num}: {lista}')
    num += 1






'''
for lista in jogos:
    for elem in lista:
        print(f'{elem:<5}', end='')
    print()
    
'''
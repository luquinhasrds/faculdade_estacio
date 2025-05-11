jogador = dict()
partidas = list()

jogador['nome'] = input('Nome do jogador: ')
jogador['partidas_jogadas'] = int(input('Foram quantas partidas jogadas: '))

for p in range(jogador['partidas_jogadas']):
    partidas.append(int(input(f'    >> Quantos gols foram feitos na {p+1}º partida:')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

print('='* 35)
for k, v in jogador.items():
    print(f'{k} = {v}')
print('='* 35)

for k, v in enumerate(partidas):
    print(f'O jogador {jogador['nome']} fez {v} gols')
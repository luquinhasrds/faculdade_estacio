jogador = dict()
partidas = list()
time = list()
id = 0

while True:
    id += 1
    jogador.clear()
    jogador['Cod'] = id
    jogador['Nome'] = input('Nome do jogador: ')
    partidas_quant = int(input('Foram quantas partidas jogadas: '))

    for p in range(partidas_quant):
        partidas.append(int(input(f'    >> Quantos gols foram feitos na {p+1}º partida:')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)

    time.append(jogador.copy())
    
    opcao = input('Cadastrar mais jogadores [S/N]?').upper()
    while True:
        if opcao in 'SN':
            break
        else:
            print('ERRO! SOMENTE S OU N !!')
    if opcao == 'N':
        break
    
    
for j in time:
    for i in j.keys():
        print(f'{i:<15}', end='')
        
    print()
for j in time:
    for i in j.values():
        print(f'{str(i):<15}', end='')
    print()


while True:
    busca = int(input('Digite ID de um jogador para ver os dados (999 para cancelar):'))

    if busca == 999:
        break
    if busca > len(busca):
        
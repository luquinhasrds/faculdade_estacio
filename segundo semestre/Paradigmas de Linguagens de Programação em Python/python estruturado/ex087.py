matrix = [[0,0,0], [0,0,0], [0,0,0]]

for linha in range(3):
    for coluna in range(3):
        matrix[linha][coluna] = int(input(f'Digite um valor para [{linha+1}, {coluna+1}]: '))
for linha in range(3):
    for coluna in range(3):
        print(f'[{matrix[linha][coluna]:^6}]', end=' ')
    print()
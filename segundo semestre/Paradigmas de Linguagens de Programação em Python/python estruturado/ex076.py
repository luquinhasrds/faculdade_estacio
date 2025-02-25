dados = ('livro', 5.99, 'bolacha', 2.66, 'caneta', 1.50, 'caderno', 10.00)

for posicao in range(0, len(dados)):
    if posicao % 2 == 0:
        print(f'{dados[posicao]:.<30}', end='')
    else:
        print(f'R${dados[posicao]:>7}')
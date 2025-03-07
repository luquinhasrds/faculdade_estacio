matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] 
soma = 0
soma_elem_terceiro = 0
maior_valor = 0

for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha+1}, {coluna+1}: ]'))
for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^6}]', end=' ')
    print()
    
for linha in matriz:
    for elem in linha:
        if elem % 2 == 0:
            soma += elem
            
for linha in matriz:
    soma_elem_terceiro += linha[2]

for n in matriz[1]:
    if n > maior_valor:
        maior_valor = n


print(F'A SOMA DOS NUMEROS DA TERCEIRA COLUNA É [{soma_elem_terceiro}]')
print(f'A SOMA DOS PARES É [{soma}]')
print(f'O maior valor da segunda linha é [{maior_valor}]')

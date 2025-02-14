frase = input('digite um frase para ver se é um palindromo: ')

frase1 = frase[::-1]

if frase1 == frase:
    print(f'a frase {frase} é um palindromo')
else:
    print('nao é um palindromo')
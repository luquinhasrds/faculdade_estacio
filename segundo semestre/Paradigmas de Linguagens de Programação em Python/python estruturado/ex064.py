contador = -1
soma = 0

while True:
    contador += 1
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    soma += n
    print(f'A soma é {soma}.')
    print(f'Foram {contador} numeros digitados.')


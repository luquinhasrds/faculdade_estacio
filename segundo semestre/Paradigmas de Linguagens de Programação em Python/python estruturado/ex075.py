tupla = tuple(int(input('digite um numero:')) for _ in range(4))

nove = tupla.count(9)

if 3 in tupla:
    tres = tupla.index(3)
    print(f'o primeiro valor 3 foi digitado na posicao {tres}.')

def Pares(item):
    for num in item:
        if num % 2 == 0:
            print(num)

print(f'apareceu {nove} vezes o numero 9.')

Pares(tupla)

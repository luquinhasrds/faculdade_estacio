tupla = tuple(int(input('digite um numero:')) for _ in range(4))

nove = tupla.count(9)

tres = tupla.index(3)

print(f'apareceu {nove} vezes o numero 9.')
print(f'o primeiro valor 3 foi digitado na posicao {tres}.')

for num in tupla:
    if num % 2 == 0:
        print(num, end=' ')

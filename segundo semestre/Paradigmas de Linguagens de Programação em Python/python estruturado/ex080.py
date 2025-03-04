lista = []
pos = 0

for num in range(5):
    numero = int(input('digite um numero:'))
    if num == 0 or numero > lista[-1]:
        lista.append(numero)
    else:
        while pos < len(lista):
            if numero <= lista[pos]:
                lista.insert(pos, numero)
                break
            pos += 1
print(lista)
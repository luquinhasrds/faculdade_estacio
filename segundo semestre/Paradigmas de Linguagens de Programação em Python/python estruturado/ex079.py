lista = list()

while True:
    valor = int(input('digite um numero [0 para parar]}:'))
    if valor == 0:
        break
    if valor not in lista:
        lista.append(valor)

lista.sort()

print(lista)
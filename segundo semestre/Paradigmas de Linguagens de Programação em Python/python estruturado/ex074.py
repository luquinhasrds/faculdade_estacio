from random import randint

lista = tuple([randint(1, 10) for numero in range(5)])


print(lista)
print(max(lista))
print(min(lista))
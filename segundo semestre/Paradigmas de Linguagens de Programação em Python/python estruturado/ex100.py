from random import randint

def sortear(lista, quant):
    lista[:] = [randint(1, 9) for x in range(quant)]
    print(f'Temos os numeros {lista}')

def somar_pares(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    print(f'a soma dos numeros pares desta lista é: {soma}')

quant = int(input('Digite quantos numeros para serem sorteados:'))

numeros = list()

sortear(numeros, quant)
somar_pares(numeros)
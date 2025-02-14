soma = 0
for numero in range(1, 7):
    num = int(input('digite um numero: '))
    if num % 2 == 0:
        soma += num
print(soma)
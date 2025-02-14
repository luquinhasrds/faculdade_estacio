comeco = int(input('digite um numero para comecar: '))
resultado = 1
for n in range(comeco, 0, -1):
    resultado = resultado * n
print(resultado)
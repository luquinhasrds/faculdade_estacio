comeco = int(input('digite o comeco: '))
passo = int(input('digite o passo: '))
decimo = comeco + 9 * passo

for numero in range(comeco, decimo + passo, passo):
    print(numero)

print('FIM')

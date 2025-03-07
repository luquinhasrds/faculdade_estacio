'''var = 1
numeros = []
par = []
impar = []

while len(numeros) <= 7:
    numeros.append(int(input(f'Digite o {var}º numero:')))
    var += 1

for n in numeros:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

impar.sort()
par.sort()
print(numeros)
print(par)
print(impar)'''


numeros = [int(input(f'Digite o {i+1}º numero:')) for i in range(7)]
par = sorted([n for n in numeros if n % 2 == 0])
impar = sorted([n for n in numeros if n % 2 != 0])
print(impar)
print(par)
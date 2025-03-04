lista = []
par = []
impar = []

while True:
    numero = int(input('Digite um numero: '))
    if numero == 0:
        break
    else:
        lista.append(numero)
        
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
        
print(f'lista original: {lista}')
print(f'lista de impar: {impar}')
print(f'lista de par  : {par}')
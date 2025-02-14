comeco = int(input('digite o comeco: '))
passo = int(input('digite o passo: '))
decimo = comeco + 9 * passo
contador = 0

while contador < 10:
    print(comeco)
    
    comeco += passo
    contador += 1
    
print('FIM')
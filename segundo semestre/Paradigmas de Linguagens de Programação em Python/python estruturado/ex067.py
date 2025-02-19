while True:
    numero = int(input('Digite um numero para a tabuada: '))
    if numero <= 0:
        break
    
    for num in range(1, 11):
        print(f'[{numero}] X [{num}] = [{numero*num}]')
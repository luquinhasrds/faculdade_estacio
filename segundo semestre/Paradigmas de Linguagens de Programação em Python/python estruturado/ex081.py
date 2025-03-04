lista = []

while True:
    numero = int(input('Digite um numero [0] para sair: '))
    if numero != 0:
        lista.append(numero)
    else:
        break
    
    
    
    
quant = len(lista)
invertido = sorted(lista, reverse=True)
    
print(f'Foram escritos {quant} numeros.')
    
print(f'a lista em forma descrescente: {invertido}')

if 5 in lista:
    print('O valor 5 foi digitado e esta na lista.')
else:
    print('Sem valor 5 na lista.')
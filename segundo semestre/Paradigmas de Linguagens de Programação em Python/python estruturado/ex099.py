def maior(* num):
    contador = maior = 0
    for numero in num:
        print(f'{numero}', end=' ', flush=True)
        if numero == 0:
            maior = numero
        elif numero > maior:
            maior = numero
        contador += 1
    print()
    print(f'O maior numero é {maior}')
    
    
entrada = input('Digite os numeros separados por espaços: ')

numeros = (int(x) for x in entrada.split())

maior(*numeros)
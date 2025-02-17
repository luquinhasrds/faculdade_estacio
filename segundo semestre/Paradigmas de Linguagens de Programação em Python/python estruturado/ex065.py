contador = 0
maior = 0
menor = None
soma = 0
opcao = 'S'

while opcao == 'S':
    while True:
        numero = int(input('Digite um numero: [0 para fechar]\n'))
        if numero == 0:
            break
        soma += numero
        contador += 1
        
        if numero > maior:
            maior = numero
        if menor is None or numero < menor:
            menor = numero

    print(f'Maior: {maior}')
    print(f'Menor: {menor}')
    print(f'Soma: {soma}')
    print(f'Media: {soma/contador}')
    
    opcao = input('Quer continuar: [S/N]\n').upper()
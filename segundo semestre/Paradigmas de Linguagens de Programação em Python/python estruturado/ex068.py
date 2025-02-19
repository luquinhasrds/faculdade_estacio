from random import randint
contador = 0

while True:
    numero = int(input('Digite um numero: [0] para fechar\n'))
    if numero == 0:
        break
    
    opcao = input('Digite (P)para par, e (I)para impar: [0] para fecharz\n').upper()
    if numero == 0:
        break
    
    pc = randint(1,11)
    soma = pc + numero
    
    
    print(f'voce escolheu [{numero}] e o pc escolheu [{pc}].')
    
    
    if soma%2 == 0 and opcao == 'P' or soma%2 != 0 and opcao == 'I':
        contador += 1
        print('='*40)
        print(f'Voce ganhou!!')
        print('='*40)
    else:
        print('x'*40)
        print('voce perdeu')
        print(f'voce ganhou {contador} consecutivas.')
        print('x'*40)
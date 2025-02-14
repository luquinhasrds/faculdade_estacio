from random import randint
from time import sleep

print('=-' * 20)
print('vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('=-' * 20)

numero = randint(1, 11)
palpite = 0

print('em que numero pensei?????')

while True:
    jogador = int(input('adivinhe o numero: '))
    palpite += 1
    if jogador == numero:
        
        print('==' * 20)
        print('voce acertou!!!!!!!')
        print(f'Foram {palpite} palpites')
        print('==' * 20)
        break
    else:
        print('==' * 20)
        print(f'ganhei pensei no numero {numero}, e nao no numero {jogador}')
        print('==' * 20)
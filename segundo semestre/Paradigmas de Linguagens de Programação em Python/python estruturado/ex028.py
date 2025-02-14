from random import randint
from time import sleep

print('=-' * 20)
print('vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('=-' * 20)

numero = randint(0, 5)

print('Pensando.....')
sleep(2)

jogador = int(input('Em que numero pensei? '))

if jogador == numero:
    print('==' * 20)
    print('Parabens, voce acertou!')
    print('==' * 20)
else:
    print('==' * 20)
    print(f'ganhei pensei no numero {numero}, e nao no numero {jogador}')
    print('==' * 20)
print('=-'*20)
velocidade = int(input('Qual a velocidade atual do carro? '))
print('=-'*20)
if velocidade <= 80:
    print('diriga com cuidado e tenha um otimo dia.')
else:
    multa = (velocidade - 80) * 7
    print(f'VOCE FOI MULTADO! Voce excedeu o limite de velocidade que é de 80km/h e foi multado em R${multa:.2f}')
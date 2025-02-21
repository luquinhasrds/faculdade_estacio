numero_extenso = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze',
                'dezesseis','dezessete','dezoito','dezenove','vinte','vinte e um','vinte e dois','vinte e tres','vinte e quatro',
                'vinte e cinco','vinte e seis','vinte e sete','vinte e oito','vinte e nove','trinta')

while True:
    numero = input('Digite um numero entreo [0 e 30] | Digite [SAIR] para sair: ').upper()
    if numero == 'SAIR':
        print('Saindo...')
        break
    
    if 0 <= int(numero) <= 30:
        print(f'O numero que voce digitou é {numero_extenso[int(numero)]}')
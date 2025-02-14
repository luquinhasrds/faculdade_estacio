produto = int(input('Qual o valor do produto? '))
print('=-' * 20)
print('FORMAS DE PAGAMENTO')
print('''
[1] a vista dinheiro/cheque
[2] a vista no cartao
[3] 2x no cartao
[4] 3x ou mais no cartao
''')

opcao = int(input('qual opcao voce deseja? '))

if opcao == 1:
    print(f'o produto de R${produto}, vai custar R${produto - (produto * 0.10)}')
elif opcao == 2:
    print(f'o produto de R${produto}, vai custar R${produto - (produto * 0.05)}')
elif opcao == 3:
    print(f'o produto de R${produto}, vai custar R${produto}')
elif opcao == 4:
    print(f'o produto de R${produto}, vai custar R${produto + (produto *0,20)}')
else:
    print('opcao invalida, tente novamente.')
from time import sleep
print('='*40)
num1 = int(input('digite um numero: '))
num2 = int(input('digite outro numero: '))

while True:
    print('''
[1]Somar
[2]Maior
[3]Multiplicar
[4]Novos numeros
[5]Sair
''')
    
    opcao = int(input('Digite qual opcao deseja: '))

    if opcao == 1:
        soma = num1 + num2
        print('-'*40)
        print(f'A soma dos numeros é {soma}')
        print('-'*40)
    elif opcao == 2:
        if num1 > num2:
            print('-'*40)
            print(f'O numero maior é {num1}')
            print('-'*40)
        else:
            print('-'*40)
            print(f'O numero maior é {num2}')
            print('-'*40)
    elif opcao == 3:
        mult = num1 * num2
        print('-'*40)
        print(f'A multiplicação dos numero {num1} e {num2} é {mult}')
        print('-'*40)
    elif opcao == 4:
        num1 = int(input('digite um numero: '))
        num2 = int(input('digite outro numero: '))
    elif opcao == 5:
        print('Fechando o programa.....')
        sleep(4)
        break
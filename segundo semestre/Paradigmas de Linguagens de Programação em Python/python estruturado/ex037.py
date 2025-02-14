numeroInt = int(input('Digite um número inteiro para conversao: '))
print('=-' * 20)

print('''
Escolha uma das bases para conversao:
[1] converter para BINARIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL
''')

opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'o numero {numeroInt} convertido para BINARIO é {bin(numeroInt)}')
elif opcao ==2:
    print(f'o numero {numeroInt} convertido para OCTAL é {oct(numeroInt)}')
elif opcao ==3:
    print(f'o numero {numeroInt} convertido para HEXADECIMAL é {hex(numeroInt)}')
else:
    print('opcao invalida, tente novamente.')
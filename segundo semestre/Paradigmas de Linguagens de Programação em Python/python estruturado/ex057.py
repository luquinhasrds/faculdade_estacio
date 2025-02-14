while True:
    opcao = input('digite o seu sexo: M/F  ')

    if opcao == 'M' or opcao == 'F':
        print('===== acertou =====')
        break
    else:
        print('tente novamente')
        print('='*30)
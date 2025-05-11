def leiaint(msg):
    ok = False
    while True:
        n = input(msg)
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('Digite um numero: ')
        if ok == True:
            break
    resultado = print(f'Voce digitou o numero {valor}')
    return resultado

leiaint('DIGITE UM NUMERO: ')
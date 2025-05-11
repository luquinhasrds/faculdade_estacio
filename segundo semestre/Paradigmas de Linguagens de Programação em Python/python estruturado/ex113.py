def leiaInt():
    while True:
        try: 
            n = int(input('Digite um numero inteiro:'))
        except:
            print('\033[31mDigite um numero inteiro valido!!!\033[m')
            continue
        else:
            return n 
        
def leiaFloat():
    while True:
        try:
            n = float(input('Digite um numero real:').replace(',', '.'))
        except:
            print('\33[31mDigite um numero real valido!!!\033[m') 
            continue
        else:
            return n

leiaInt()
leiaFloat()
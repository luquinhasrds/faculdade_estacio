
cinquenta = vinte = dez = cinco = dois = um = 0

while True:
    valor = int(input('Qual o valor a ser sacado: '))
    
    if valor >= 50:
        cinquenta = valor // 50
        valor = valor % 50
    
    if valor >= 20:
        vinte = valor // 20
        valor = valor % 20
    
    if valor >= 10:
        dez = valor // 10
        valor = valor % 10
    
    if valor >= 5:
        cinco = valor // 5
        valor = valor % 5
    

    if valor >= 2:
        dois = valor // 2
        valor = valor % 2
    
    if valor >= 1:
        um = valor // 1
        valor = valor % 1

    if cinquenta > 0:
        print(f"{cinquenta} notas de R$50")
    if vinte > 0:
        print(f"{vinte} notas de R$20")
    if dez > 0:
        print(f"{dez} notas de R$10")
    if cinco > 0:
        print(f"{cinco} notas de R$5")
    if dois > 0:
        print(f"{dois} notas de R$2")
    if um > 0:
        print(f"{um} moeda de R$1")
    
    opcao = input('Deseja realizar outro saque? [S/N]: ').upper()
    if opcao == 'N':
        break 



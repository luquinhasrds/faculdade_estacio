comeco = int(input('digite o comeco: '))
passo = int(input('digite o passo: '))
decimo = comeco + 9 * passo
contador = 0

a_mais = 10
total = 0

while a_mais != 0:
    total = a_mais + total

    while contador < total:
        print(comeco)
        
        comeco += passo
        contador += 1


    a_mais = int(input('quer mostrar mais termos, se sim, quantos? '))


print('FIM')
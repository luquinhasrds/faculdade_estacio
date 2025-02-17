n1 = int(input('Digite um numero para iniciar '))    
contador = 0
num1=0
num2=1

while contador < n1:
    soma = num1 + num2
    num1 = num2
    num2 = soma
    contador += 1
    print(soma, end=' - ')
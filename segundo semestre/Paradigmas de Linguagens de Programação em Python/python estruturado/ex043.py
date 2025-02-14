peso = int(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))
imc = peso / (altura ** 2)
print('=-' * 20)

if imc < 18.5:
    print(f'voce esta abaixo do peso, seu IMC é {imc:.2f}') 
elif imc >= 18.5 and imc < 25:
    print(f'voce esta no peso ideal, seu IMC é {imc:.2f}')
elif imc >= 25 and imc < 30:
    print(f'voce esta com sobrepeso, seu IMC é {imc:.2f}')
elif imc >= 30 and imc < 40:
    print(f'voce esta com obesidade, seu IMC é {imc:.2f}')
else:
    print(f'voce esta com obesidade morbida, seu IMC é {imc:.2f}')
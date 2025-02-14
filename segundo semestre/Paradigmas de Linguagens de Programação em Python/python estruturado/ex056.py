mulheres_menos_vinte = 0
maior = 0
media = 0
soma= 0
nome_velho = ''

for pessoas in range(1, 5):
    nome = input('Digite o seu nome: ')
    idade = int(input('digite sua idade: '))
    sexo = input('digite o seu sexo: [M/F]: ')

    print('='*40)

    soma += idade 
    media = soma / pessoas

    if sexo == 'M' and idade > maior:
        maior = idade
        nome_velho = nome

    if sexo == 'F' and idade < 20:
        mulheres_menos_vinte += 1
    
print(f'A media de idade do grupo é de {media}')
print(f'O nome do homem mais velho é {nome_velho}')

if mulheres_menos_vinte == 0:
    print('nao tem mulheres no grupo')
else:
    print(f'A quantidade de mulheres ABAIXO de 20 anos é de {mulheres_menos_vinte}')
homens = 0
mulheres = 0
pessoas = 0

while True:
    idade = int(input('Digite sua idade:'))
    sexo = input('Seu sexo [M/F]:').upper()
    opcao = input('Quer continuar [S/N]?').upper()

    if idade > 18:
        pessoas += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    if opcao == 'N':
        break


print(f'Pessoas +18: {pessoas}')
print(f'Homens cadastrados: {homens}')
print(f'mulheres com +20: {mulheres}')
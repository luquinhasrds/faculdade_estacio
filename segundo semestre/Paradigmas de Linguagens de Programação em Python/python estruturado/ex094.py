pessoa = dict()
pessoas = list()
soma_idade = 0
while True:
    pessoa.clear()
    pessoa['nome'] = input('Digite o nome:')
    while True:
        pessoa['sexo'] = input('Digite seu sexo [M / F]:').upper() [0]
        if pessoa['sexo'] in 'MF':
            break
        else:
            print('Erro! somente M ou F.')
    pessoa['sexo'] == 'F'
    pessoa['idade'] = int(input('Digite sua idade:'))
    
    soma_idade += pessoa['idade']
    pessoas.append(pessoa.copy())
    
    
    while True:
        opcao = input('Quer cadastras mais pessoas [S / N]?').upper() [0]
        if opcao in 'SN':
            break
        else:
            print('ERRO! somente S ou N.')
            continue
    if opcao == 'N':
        break

print('=' * 50)

cadastradas = len(pessoas)
media = soma_idade / cadastradas

print(f'Foram cadastradas {cadastradas} pessoas.')
print('-' * 35)

print(f'A media de idade é {media:.2f}')
print('-' * 35)

print('Mulheres:')
for mulher in pessoas:
    if mulher['sexo'] == 'F':
        for k, v in mulher.items():
            print(f'{k} = {v}')
    print('_'*30)
print('-' * 35)

print('Pessoas com idade acima da media:')
for pessoa in pessoas:
    if pessoa['idade'] >= media:
        for k, v in pessoa.items():
            print(f'{k} = {v};')
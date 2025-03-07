pessoa = []
pessoas = []
pesadas = []
leves = []
while True:
    print('----cadastro de pessoas----')
    pessoa.append(str(input('Digite seu nome: ').upper()))
    pessoa.append(int(input('Digite seu peso: ')))
    pessoas.append(pessoa[:])
    pessoa.clear()
    opcao = input('Cadastrar mais uma pessoa [S/N]? ').upper()
    if opcao == 'S':
        continue
    else:
        break

quant = len(pessoas)

for p in pessoas:
    if p[1] > 50:
        pesadas.append(p[0])
    else:
        leves.append(p[0])

print(f'A quantidade de pessoas cadastradas é: {quant}')
print(f'Pessoas pesadas: {pesadas}')
print(f'Pessoas leves: {leves}')
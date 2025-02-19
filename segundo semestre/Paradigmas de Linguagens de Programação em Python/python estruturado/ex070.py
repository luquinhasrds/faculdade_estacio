total = 0
mais_1000 = 0
mais_barato = None
nome = ''
soma = 0

while True:
    produto = input('Qual o nome do produto: ').upper()
    valor = float(input('Digite o valor do produto [decimal separado por ponto] : '))
    
    
    soma += valor
    
    if valor > 1000:
        mais_1000 += 1
    if mais_barato is None or valor < mais_barato:
        mais_barato = valor
        nome = produto
    
    opcao = input('Quer continuar [S/N]?').upper()
    if opcao == 'N':
        break

print(f'Produtos com valor acima de 1000: {mais_1000}')
print(f'O produto mais barato foi {nome}, que custa {mais_barato}')
print(f'Total gasto: {soma}')
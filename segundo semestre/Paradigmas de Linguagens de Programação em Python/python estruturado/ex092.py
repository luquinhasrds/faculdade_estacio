pessoa = dict()
import datetime
ano_atual = datetime.datetime.now().year

pessoa['Nome'] = input('Digite seu nome:')
pessoa['Ano_Nascimento'] = int(input('Digite o ano de nascimento:'))
pessoa['Carteira_trabalho'] = input('Digite o numero da carteira de trabalho (se possuir):').strip()
pessoa['idade'] = ano_atual - pessoa['Ano_Nascimento']

if pessoa['Carteira_trabalho'] != '':
    pessoa['Ano_de_contratação'] = int(input('Digite o ano de contratação: '))
    pessoa['salario'] = float(input('Digite seu salario: '))
    pessoa['Aposentadoria'] = pessoa['idade'] + ((pessoa['Ano_de_contratação'] + 35) - ano_atual)
else:
    pessoa['Carteira_trabalho'] = 'Sem carteira'
print('-'*40)
for k, v in pessoa.items():
    print(f'{k} = {v}')
print('-'*40)
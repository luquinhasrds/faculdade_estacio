aluno = dict()

aluno['Nome'] = str(input('Nome do aluno: '))
aluno['Media'] = int(input('Media do aluno (0 a 10): '))

if aluno['Media'] > 6:
    aluno['Situação'] = 'Aprovado'
elif aluno['Media'] <= 3:
    aluno['Situação'] = 'Reprovado'
else:
    aluno['Situação'] = 'Recuperação'
    
for k, v in aluno.items():
    print(f'{k} = {v}')
alunos = []
aluno = []
num = 1

while True:
    id = (num)
    num += 1
    nome = input('Nome: ')
    nota1 = int(input('Nota 1: '))
    nota2 = int(input('Nota 2: '))
    media = ((nota1+nota2)/2)
    alunos.append([id, nome, [nota1, nota2], media])
    aluno.clear()
    
    if input('Quer contunuar [S/N]').upper() != 'S':
        break

print(f'{'No.':<5}{'Nome':<20}{'Media':<10}')
print('-'*30)
for a in alunos:
    print(f'{a[0]:<5}{a[1]:<20}{a[3]:<20.2f}')
    
while True:
    opcao = int(input('Digite o numero do aluno [999 finaliza]:'))
    
    if opcao == 999:
        break 
    if opcao <= len(alunos)  and opcao > 0:
        print(f'As notas DE {alunos[opcao-1][1]} são {alunos[opcao-1][2]}')
print('-'*30)
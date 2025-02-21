frase = input('digite uma frase qualquer: ')

a = frase.count('a')

posicao = frase.find('a')

posicao_final = frase.rfind('a')



print(f'a frase tem {a} "A".')

if posicao != -1:
    print(f'{posicao}º posição')
else:
    print('nao tem letras "a" na frase.')

if posicao_final != -1:
    print(f'{posicao_final}º posição')
else:
    print('nao tem letras "a" na frase.')

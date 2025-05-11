from time import sleep

def contador(i, f, p):
    print(f'contagem de {i} a {f} de {p} em {p}')
    
    if i < f:
        count = i
        while count <= f:
            print(count, end=' ', flush=True)
            sleep(0.5)
            count += p
    else:
        count = i
        while count >= f:
            print(count, end=' ', flush=True)
            sleep(0.5)
            count -= p
print('~' * 40)
print(contador(1, 10, 1))
print(contador(10, 0, 2))

print('~' * 40)
print()
print('Agora com numeros personalizados!!')
inicio = int(input(' => INICIO: '))
fim = int(input(' => FIM: '))
passo = int(input(' => PASSO: '))
print('=' * 30)
contador(inicio, fim, passo)
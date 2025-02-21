numero = int(input('digite um numero entre [0 e 9999]: '))

m = numero // 1000 % 10
c = numero // 100 % 10
d = numero // 10 % 10
u = numero // 1 % 10

print(f'Milhar = {m}')
print(f'Centena = {c}')
print(f'Dezena = {d}')
print(f'Unidade = {u}')
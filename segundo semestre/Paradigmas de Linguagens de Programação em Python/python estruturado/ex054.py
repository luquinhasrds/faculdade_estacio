pessoas1 = 0
pessoas2 = 0

for nasc in range(1, 8):
    nasc = int(input('digite o ano de nascimento: '))
    if 2025 - nasc  < 18:
        pessoas1 += 1
        pass
    elif 2025 - nasc >= 18:
        pessoas2 += 1

print(f'{pessoas1} pessoas nao atingiram maioridade')
print(f'{pessoas2} pessoas atingiram maioridade')
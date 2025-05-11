def fatorial(num=1):
    fatorial = 1
    for n in range(num, 0, -1):
        fatorial *= n
    return fatorial

print(fatorial(5))
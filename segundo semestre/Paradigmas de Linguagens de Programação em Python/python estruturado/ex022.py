nome = input('Digite seu nome completo: ')

print(nome.upper())



print(nome.lower())



nome_sem_espacos = nome.replace(' ', '')

print(len(nome_sem_espacos))



lista_palavras = nome.split()

primeiro_palavra = len(lista_palavras[0])

print(primeiro_palavra)
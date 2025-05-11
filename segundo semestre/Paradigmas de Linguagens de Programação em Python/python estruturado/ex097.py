def escreva(text):
    caract = len(text)
    print('~' * (caract))
    print(text)
    print('~' * (caract))

while True:
    escreva(input('Digite o que quiser: '))
    if escreva == 'Sair':
        break
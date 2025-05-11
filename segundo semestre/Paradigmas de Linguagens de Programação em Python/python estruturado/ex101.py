import datetime
ano_atual = datetime.datetime.now().year

def voto(ano):
    
    idade = ano_atual - ano
    if idade >= 18:
        voto = print(f'Com {idade} anos: O SEU VOTO É OBRIGATORIO!!!!.')
    elif idade < 16:
        voto = print(f'Com {idade} anos: VOCE NAO PODE VOTAR!')
    else:
        voto = print(f'Com {idade} anos: O SEU VOTO É OPCIONAL.')
    return voto

dado = int(input('Digite seu ano de nascimento:'))

voto(dado)
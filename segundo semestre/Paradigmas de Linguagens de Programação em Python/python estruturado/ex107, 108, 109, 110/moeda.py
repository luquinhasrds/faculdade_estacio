def aumentar(valor=0, taxa=0, formato = False):
    aumenta = valor + taxa
    return aumenta if formato is False else moeda(aumenta)

def diminuir(valor=0, taxa=0, formato = False):
    diminui = valor - taxa
    return diminui if formato is False else moeda(diminui)

def dobro(valor=0, formato = False):
    dobro = valor*2
    return dobro if formato is False else moeda(dobro)

def metade(valor=0, formato = False):
    metade = valor/2
    return metade if formato is False else moeda(metade)

def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')

def resumo(valor=0, taxa_aumento=10, taxa_reducao=5):
    print(f'''
        =================================================
        Valor  = {moeda(valor)}
        Dobro  = {dobro(valor, True)}
        Metade = {metade(valor, True)}
        Com {taxa_aumento}% de aumento = {aumentar(valor, taxa_aumento, True)}
        Com {taxa_reducao}% de redução = {diminuir(valor, taxa_reducao, True)}
        =================================================
        ''')
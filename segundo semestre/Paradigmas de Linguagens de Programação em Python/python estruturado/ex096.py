def area_quadrado(largura, comprimento):
    area = largura * comprimento
    return print(f'AREA: {largura} X {comprimento} = {area}')

comprimento = float(input('COMPRIMENTO (M): '))
largura = float(input('LARGURA (M): '))
area_quadrado(largura, comprimento)
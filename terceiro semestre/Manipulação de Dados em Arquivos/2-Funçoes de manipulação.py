print('escreva frases e sair para finalizar:')
frases = []
while True:
    frase = input('digite uma frase: ')
    if frase == 'SAIR':
        break
    frases.append(frase)
    
with open('2;2-arquivo_com_frases', 'w', encoding='utf-8') as arquivo:
    for frase in frases:
        arquivo.write(frase + '\n')
        
        
dados_modificados = []

with open('2;2-arquivo_com_frases') as arquivo:
    for linha in arquivo:
        dados_modificados.append(linha.strip().upper())
        

with open('2;2-arquivo_com_frases', 'w') as arquivo:
    for linha in dados_modificados:
        arquivo.write(linha + '\n')


def zenit_polar(text):
    replacent = [("z", "p"), ("e", "o"), ("n", "l"), ("i", "a"), ("t", "r"),  #MINUSCULO
                ("Z", "P"), ("E", "O"), ("N", "L"), ("I", "A"), ("T", "R")]  #MAIUSCULO
    for old, new in replacent:
        text = text.replace(old, new)
    return text
        

        
texto = "O vento passava entre as árvores como se estivesse contando segredos que só elas podiam entender. No meio da rua quase vazia, um gato preto atravessou lentamente, parando por alguns segundos como se estivesse avaliando o destino de quem o observava. Mais adiante, um senhor caminhava com uma sacola de pão fresco, enquanto o aroma se espalhava e misturava-se ao cheiro de terra molhada da chuva que havia caído minutos antes."

convert = texto.split()

coded = [zenit_polar(words) for words in convert]

coded_new = ' '.join(coded)
print(coded_new)


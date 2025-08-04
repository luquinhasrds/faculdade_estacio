import os


arquivo1 = open('exemplo', 'w', encoding='utf-8')
arquivo1.write('Olá, mundo!!!!')
arquivo1.close()

arquivo1 = open('exemplo', 'r', encoding='utf-8')
print(arquivo1.read())
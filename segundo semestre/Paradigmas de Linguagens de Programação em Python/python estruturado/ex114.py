import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('o site nao foi encontrado :(')
else:
    print('O SITE FOI ENCONTRADO!!!!!  :)')
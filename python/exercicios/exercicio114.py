import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site do pudim não está disponível!!!')
else:
    print('Consegue acessar o site do pudim')
#Python3 
#verificaProfileTwitter.py - esse script verifica se o perfil do twitter existe.

import requests
from bs4 import BeautifulSoup
'''
proxies = {
 'http': 'seu.proxy',
 'https': 'seu.proxy',
}
'''
arq1 = open('teste1.txt', 'r')
arq2 = open('twitter_profiles_true.txt', 'a')

count = 0
countSucesso = 0
countFracasso = 0

linha = arq1.readline()
while linha:
    twitterLink = linha
    #print(twitterLink)
    #req = requests.get(twitterLink.strip(), proxies=proxies)
    req = requests.get(twitterLink.strip())
    #print(req)
    if req.status_code == 200:
        print('Requisição bem sucedida!')
        countSucesso += 1
        arq2.write(twitterLink)
    else:
        print('Pagina nao encontrada')
        countFracasso += 1
    linha = arq1.readline()
    count += 1

print(count)
print(countSucesso)
print(countFracasso)    
print('Done...')

arq1.close()
arq2.close()


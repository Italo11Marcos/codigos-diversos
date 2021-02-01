#Python3 
#verificaProfileFacebook.py - esse script verifica se o perfil do facebook existe.

import requests
from bs4 import BeautifulSoup
'''
proxies = {
 'http': 'seu.proxy',
 'https': 'seu.proxy',
}
'''
arq1 = open('teste1.txt', 'r')
arq2 = open('facebook_profiles_true.txt', 'a')

count = 0
countSucesso = 0
countFracasso = 0

linha = arq1.readline()
while linha:
    facebookLink = linha
    #print(facebookLink)
    #req = requests.get(facebookLink.strip(), proxies=proxies)
    req = requests.get(facebookLink.strip())
    #print(req)
    if req.status_code == 200:
        print('Requisição bem sucedida!')
        countSucesso += 1
        arq2.write(facebookLink)
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


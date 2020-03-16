#Python3 
#verificaProfileFacebook.py - esse script verifica se o perfil do facebook existe.

import requests
from bs4 import BeautifulSoup
'''
proxies = {
 'http': seu.proxy
 'https': seu.proxy
}
'''
arq1 = open('instagram_profiles.txt', 'r')
arq2 = open('instagram_profiles_true.txt', 'w')

count = 0
countSucesso = 0
countFracasso = 0

linha = arq1.readline()
while linha:
    instagramLink = linha
    #print(instagramLink)
    #req = requests.get(instagramLink.strip(), proxies=proxies)
    req = requests.get(instagramLink.strip())
    #print(req)
    if req.status_code == 200:
        print('Requisição bem sucedida!')
        countSucesso += 1
        arq2.write(instagramLink)
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


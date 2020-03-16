from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import requests
import os
import shutil
'''
proxies = {
 'http': 'seu.proxy',
 'https': 'seu.proxy',
}
'''
arq = open('linkPokeSprite', 'w')

req_url = 'https://pokemondb.net/pokedex/all'
#req = requests.get(req_url, proxies=proxies)
req = requests.get(req_url)
soup = BeautifulSoup(req.content, 'html.parser')
print('chegou aqui')
images = soup.find_all('img')
for image in images:
    print('aqui')
    print(image.get('image-src'))

arq.close()
'''
###################
'''
#Caminho da pasta onde as imagens ficarão salvas
folder = '/home/dti/Documentos/WebScrapping/pokemonSprites'
#Caminho da imagem
fileimg = '/home/dti/Documentos/WebScrapping/'
'''
counter = 0
arq = open('linkPokeSprite', 'r')
linha = arq.readline()
while linha:
    link = linha
    #set stream to True, this will return the stream content
    req = requests.get(link.strip(), proxies=proxies, stream=True)
    local_file = open(str(counter)+'.png', 'wb')
    #Move a imagem para a pasta imagens
    shutil.move(fileimg+str(counter)+'.png',folder)
    counter += 1
    print('Salvando imagem...')
    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
    req.raw.decode_content = True
    # Copy the response stream raw data to local image file.
    shutil.copyfileobj(req.raw, local_file)
    # Remove the image url response object.
    del req
    linha = arq.readline()
print('Terminando...')
arq.close()
print('Done')
'''
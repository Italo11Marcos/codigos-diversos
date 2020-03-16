#from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import requests
import os
import shutil

proxies = {
 'http': 'seu.proxy',
 'https': 'seu.proxy',
}

arq = open('linkIMG.txt', 'w')

req_url = 'https://en.wikipedia.org/wiki/Peter_Jeffrey_(RAAF_officer)'
req = requests.get(req_url, proxies=proxies)
soup = BeautifulSoup(req.content, 'html.parser')
images = soup.find_all('img', {'src':re.compile('.jpg')})
for image in images: 
    print(image['src']+'\n')
    linkimg = image['src']
    linksImgs = linkimg.split('//')
    arq.write('https://'+linksImgs[1]+'\n')
print('Links gravados com sucesso')

arq.close()
'''
###################
'''
#Caminho da pasta onde as imagens ficarão salvas
folder = '/home/dti/Documentos/WebScrapping/images'
#Caminho da imagem
fileimg = '/home/dti/Documentos/WebScrapping/'

counter = 0
arq = open('linkIMG.txt', 'r')
linha = arq.readline()
while linha:
    link = linha
    #set stream to True, this will return the stream content
    req = requests.get(link.strip(), proxies=proxies, stream=True)
    local_file = open(str(counter)+'.jpg', 'wb')
    #Move a imagem para a pasta imagens
    shutil.move(fileimg+str(counter)+'.jpg',folder)
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

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import requests

proxies = {
 'http': 'seu.proxy',
 'https': 'seu.proxy',
}

req_url = 'https://en.wikipedia.org/wiki/Peter_Jeffrey_(RAAF_officer)'
req = requests.get(req_url, proxies=proxies)
soup = BeautifulSoup(req.content, 'html.parser')
images = soup.find_all('img', {'src':re.compile('.jpg')})
for image in images: 
    print(image['src']+'\n')
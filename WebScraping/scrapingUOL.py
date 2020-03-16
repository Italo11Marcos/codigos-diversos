import requests
from bs4 import BeautifulSoup


user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'

url = 'https://noticias.uol.com.br/'

req = requests.get(url , headers={'User-Agent': user_agent})

soup = BeautifulSoup(req.content, 'html.parser')

for div in soup.findAll('div',attrs={'class':'thumb-caption col-sm-24 col-xs-4 no-gutter-sm no-gutter-md no-gutter-lg'}):
    h3=div.find('h3', attrs={'class':'thumb-title'})
    print(h3.text) 
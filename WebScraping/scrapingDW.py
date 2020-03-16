#Python3
#scrapingDW.py - baixa as principais notícias da columa 'Alemanha' do site DW
#Author - Ítalo Marcos

import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrapingDW(url, proxies):

    titles_h2 = []
    links = []

    req = requests.get(url, proxies=proxies)
    soup = BeautifulSoup(req.content, 'html.parser')
    for div in soup.find_all('div', attrs={'data-id':'19329608'}):
        h2 = div.find_all('h2', attrs={'class':''})
        link = div.find_all('a')
        for i in range (len(h2)):
            titles_h2.append(h2[i].text.strip())
            links.append('https://www.dw.com/'+link[i+1]['href'])
    df = pd.DataFrame({'Titles:': titles_h2, 'Links': links})
    df.to_csv('scrapingDW.csv', index=False, encoding='latin-1')        

def main():
    url = 'https://www.dw.com/pt-br/not%C3%ADcias/s-7111'
    proxies = {
    'http': 'http://italo.siqueira:wer090122@proxy.campus.unimontes.int:3128',
    'https': 'http://italo.siqueira:wer090122@proxy.campus.unimontes.int:3128',
    }
    scrapingDW(url,proxies)

if __name__ == "__main__":
    main()
#Python3
#scrapingHacknoon.py - Scraping do título, autor e data das postagens do site Hacknoon
#Author - Ítalo Marcos

import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrapingHacknoon(url, proxies, user_agent):
    
    titles = []
    authors = []
    links = []

    req = requests.get(url, proxies=proxies)
    soup = BeautifulSoup(req.content, 'html.parser')
    for div in soup.find_all('div', attrs={'class':'story-card'}):
        title = div.find('div', attrs={'class':'title'})
        author_date = div.find('div', attrs={'class':'bio'})
        link = div.find('a')
        titles.append(title.text.strip())
        authors.append(author_date.text.strip())
        links.append('https://hackernoon.com'+link['href'])

    df = pd.DataFrame({'Title': titles, 'Author': authors, 'Link': links})
    df.to_csv('Hacknoon.csv', index=False, encoding='utf-8')

def main():

    url = 'https://hackernoon.com/tagged/coding'
    proxies = {
    'http': 'http://italo.siqueira:wer090122@proxy.campus.unimontes.int:3128',
    'https': 'http://italo.siqueira:wer090122@proxy.campus.unimontes.int:3128',
    }
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'

    scrapingHacknoon(url, proxies, user_agent)

if __name__ == "__main__":
    main()

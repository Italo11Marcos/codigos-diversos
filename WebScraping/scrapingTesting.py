from urllib.request import Request, urlopen
import urllib.request
from bs4 import BeautifulSoup as soup
import pandas as pd

#se houver proxy, caso contrário se pode comentar
proxy_support = urllib.request.ProxyHandler({'http' : 'seu.proxy', 
                                             'https': 'seu.proxy'})

opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)

url = 'http://www.pythonscraping.com/pages/page3.html'

titles = []
descriptions = []
costs = []

gifts = ['gift1','gift2','gift3','gift4','gift5']

with urllib.request.urlopen(url) as response:

    req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})

    webpage = urlopen(req).read()
    page_soup = soup(webpage, "html.parser")
    for i in gifts:
        for tr in page_soup('tr', id=i):
            tr1 = (tr.findAll('td'))
            titles.append(tr1[0].text)
            descriptions.append(tr1[1].text)
            costs.append(tr1[2].text)

    df = pd.DataFrame({'Title': titles,'Description': descriptions, 'Cost': costs})
    df.to_csv('giftList.csv', index=False, encoding='utf-8')
from urllib.request import Request, urlopen
import urllib.request
from bs4 import BeautifulSoup as soup
import pandas as pd

proxy_support = urllib.request.ProxyHandler({'http' : 'seu.proxy', 
                                             'https': 'seu.proxy'})

opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)

url = ''

with urllib.request.urlopen(url) as response:

    req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})

    webpage = urlopen(req).read()
    page_soup = soup(webpage, "html.parser")
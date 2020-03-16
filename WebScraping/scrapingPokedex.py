import requests
from bs4 import BeautifulSoup
import pandas as pd

proxies = {
 'http': 'seu.proxy',
 'https': 'seu.proxy',
}

def scrapPokedex(url):
    final_df = pd.DataFrame()
    req = requests.get(url, proxies=proxies)
    soup = BeautifulSoup(req.content, 'html.parser')
    table = soup.find('table', {'id':'pokedex'})
    df = pd.read_html(str(table))[0]
    final_df = final_df.append(df)
    return final_df

url = 'https://pokemondb.net/pokedex/all'

df = scrapPokedex(url)
df.to_csv('dataPokedex.csv', index=False, encoding='utf-8')

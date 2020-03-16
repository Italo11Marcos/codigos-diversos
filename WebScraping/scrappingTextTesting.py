import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import seaborn as sns

proxies = {
 'http': 'seu.proxy',
 'https': 'seu.proxy',
}

def scrape_table(base_url):

    final_df = pd.DataFrame()
    req = requests.get(base_url, proxies=proxies)
    soup = BeautifulSoup(req.content, 'html.parser')
    table = soup.find('table', {'id':'giftList'})
    df = pd.read_html(str(table))[0]
    final_df = final_df.append(df)
    return final_df

url = 'http://www.pythonscraping.com/pages/page3.html'
df = scrape_table(url)
df.to_csv('giftListTest.csv', index=False, encoding='utf-8')
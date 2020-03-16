import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
#import seaborn as sns

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

proxies = {
 'http': 'seu.proxy',
 'https': 'seu.proxy',
}

def scrape_stats(base_url, year):

    final_df = pd.DataFrame()

    print('Extraindo ano {}'.format(year))
    req_url = base_url.format(year)
    req = requests.get(req_url, proxies=proxies)
    soup = BeautifulSoup(req.content, 'html.parser')
    table = soup.find('table', {'id':'standings'})
    df = pd.read_html(str(table))[0]
    #df['Year'] = year
    final_df = final_df.append(df)
    return final_df

url = 'https://www.hockey-reference.com/leagues/NHL_{}_standings.html'
df = scrape_stats(url, 2018)

drop_indexes = df[df['Rk'] == 'Rk'].index # Pega indexes onde a coluna 'Rk' possui valor 'Rk'
df.drop(drop_indexes, inplace=True) # elimina os valores dos index passados da tabela

#numeric_cols = df.columns.drop(['Player','Pos','Tm'])
#df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric)

sorted_df = df.sort_values(by=['WES'], axis=0, ascending=False)
sorted_df[['Unnamed: 1', 'WES']].head()

print('ok')

df.to_csv('dataNHL.csv', index=False, encoding='utf-8')

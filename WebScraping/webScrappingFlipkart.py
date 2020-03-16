from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import pandas as pd




url = 'https://www.flipkart.com/laptops/</a>~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniq'
req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})

products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product


webpage = urlopen(req).read()
page_soup = soup(webpage, "html.parser")
for a in page_soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
    name=a.find('div', attrs={'class':'_3wU53n'})
    price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
    #rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
    products.append(name.text)
    prices.append(price.text)
    #ratings.append(rating.text) 

#df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings})
df = pd.DataFrame({'Product Name':products,'Price':prices}) 
df.to_csv('products.csv', index=False, encoding='utf-8')
import requests
from bs4 import BeautifulSoup
from collections import Counter
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

#URL a ser utilizida
url = 'https://en.wikipedia.org/wiki/Argentina'

#Faz a requisição da URL
req = requests.get(url)

#Se a requisiao for bem sucedida
if req.status_code == 200:

    #Conteudo da requisição
    html_doc = req.content

    #Objeto de BeautifulSoup
    soup = BeautifulSoup(html_doc, 'html.parser')

    #Recupera o texto do objeto
    text = soup.get_text().split()

    #transforma as palavras para forma minuscula
    for i in range(len(text)):
        text[i] = text[i].lower()

    #As 15 palavras mais comuns do texto
    print(Counter(text).most_common(15))


    comment_words = " ".join(t for t in text)
    stopwords = set(STOPWORDS)
    stopwords.update(['the', 'of', 'and', 'in', '^', 'a', 'to', 'on', 'is'])

    wordcloud = WordCloud(width=800, height=800,
                          background_color='white',
                          stopwords=stopwords,
                          min_font_size=10).generate(comment_words)

    # plot the WordCloud image
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)

    plt.show()
else:
    print('Fail')


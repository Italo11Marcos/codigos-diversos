'''
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
try:
    html = urlopen("https://www.camilaporto.com.br/blog/")
except HTTPError as e:
    print(e)
except URLError:
    print("Server down or incorrect domain")
else:
    res = BeautifulSoup(html.read(),"html5lib")
    #tags = res.findAll("h1", {"class": "post-title"})
    tags = res.findAll('span', 'a')
    for tag in tags:
        print(tag.getText())
'''
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
try:
    url = 'https://www.camilaporto.com.br/blog/'
    req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})
except HTTPError as e:
    print(e)
except URLError:
    print("Server down or incorrect domain")
else:
    webpage = urlopen(req).read()
    page_soup = soup(webpage, "html.parser")
    title = page_soup.find("title")
    print(title.getText())
    containers = page_soup.findAll("p")
    for container in containers:
        print(container.getText())

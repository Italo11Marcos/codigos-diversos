import requests
from bs4 import BeautifulSoup

url = "https://covid.ourworldindata.org/data/owid-covid-data.json"

r = requests.get(url)

last_indice = len(r.json()['BRA']['data']) - 1

print(r.json()['BRA']['data'][last_indice]['new_cases'])
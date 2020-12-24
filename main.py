import requests
from bs4 import BeautifulSoup

base_url = "https://statusinvest.com.br"
all_stocks_path = "/acao/companiesnavigation?page=1&size=1000"


all_stocks = requests.get(base_url+all_stocks_path)

stock = requests.get(base_url+"/"+all_stocks.json()[0]['url'])

soup = BeautifulSoup(stock.content, 'html.parser')

data = soup.select(' div.top-info .info')
print(data[0].contents[0])#<class 'bs4.element.NavigableString'>
# print(data.contents[0])
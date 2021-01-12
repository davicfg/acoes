import requests
from bs4 import BeautifulSoup


base_url = "https://statusinvest.com.br"
all_stocks_path = "/acao/companiesnavigation?page=1&size=1000"


all_stocks = requests.get(base_url+all_stocks_path)

stock = requests.get(base_url+"/"+all_stocks.json()[0]['url'])

soup = BeautifulSoup(stock.content, 'html.parser')

#Achando o P/L da ação
PL = soup.find_all('div',attrs={'title': 'Dá uma ideia do quanto o mercado está disposto a pagar pelos lucros da empresa.'})[0].find('strong').string
print(PL)
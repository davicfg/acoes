import csv
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
urlFundamentosAcao = 'https://www.fundamentus.com.br/detalhes.php?papel='
with open('acoes_bolsa.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
      print(urlFundamentosAcao+row[0])
      detalhesAcao = requests.get(urlFundamentosAcao+row[0], headers=headers)
      print(detalhesAcao.content) 
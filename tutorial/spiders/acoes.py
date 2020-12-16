import scrapy

class AcoesSpider(scrapy.Spider):
  name = "acoes"
  start_urls = ["https://www.fundamentus.com.br/detalhes.php"]
  user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
  def parse(self, response):
    links = response.xpath("//tbody/descendant::a/@href")

    for link in links:
      print(link)
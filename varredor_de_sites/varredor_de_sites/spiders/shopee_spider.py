import scrapy
from scrapy.crawler import CrawlerProcess


class ShopeeProductSpider(scrapy.Spider):
    # Identidade
    name = 'shopeebot'

#     Host: 127.0.0.1:65432
#   Connection: keep-alive
#   Cache-Control: max-age=0
#   sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"
#   sec-ch-ua-mobile: ?0
#   sec-ch-ua-platform: "Windows"
#   Upgrade-Insecure-Requests: 1
#   User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36
#   Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
#   Sec-Fetch-Site: none
#   Sec-Fetch-Mode: navigate
#   Sec-Fetch-User: ?1
#   Sec-Fetch-Dest: document
#   Accept-Encoding: gzip, deflate, br
#   Accept-Language: en-US,en;q=0.9
    # HEADERS = {
    #     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    #     "Accept-Encoding": "gzip, deflate, br, zstd",
    #     "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    #     "Connection": "keep-alive",
    #     "Host": "127.0.0.1:65432",
    #     "Cache-Control": "max-age=0",
    #     'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    #     "sec-ch-ua-mobile": "?0",
    #     "sec-ch-ua-platform": "Windows",
    #     "Upgrade-Insecure-Requests": "1",
    #     "Sec-Fetch-Dest": "empty",
    #     "Sec-Fetch-Mode": "cors",
    #     "Sec-Fetch-Site": "same-site",
    #     "Sec-Fetch-User": "?1",
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
    # }
    # Request

    def start_requests(self):
        # Definir urls a serem varridos
        urls = ['https://shopee.com.br/search?keyword=tapete']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # Response
    def parse(self, response):
        for element in response.xpath("//ul[@class='row shopee-search-item-result__items']//li"):
            yield {
                'Preco': element.xpath(".//div[@class='truncate flex items-baseline']//span[2]/text()").get(),
                'Link': element.xpath(".//a[@class='contents']/@href").get()
            }


bot = CrawlerProcess(
    settings={
        "FEEDS": {
            "report.csv": {"format": "csv"}
        }
    }
)

from scrapy.spider import BaseSpider
from scrapy.http import Request
from scrapyGold.items import ScrapygoldItem

class GoldSpider(BaseSpider):
    name = 'gold'
    allowed_domains = ['indiagoldrate.com']
    max_cid = 10
    rate = 10
    def __init__(self):
        self.download_delay = 1/float(self.rate)

    def start_requests(self):
        for i in range(self.max_cid):
            yield Request('http://chennai.indiagoldrate.com/?page=%d' % i,
                    callback=self.parse)

    def parse(self, response):
        goldItem = ScrapygoldItem()
        goldItem['rate'] = response.xpath('//table/tr/td[3]/table/tr[1]/td[2]/text()').extract()
        goldItem['date'] = response.xpath('//tr/td/a[@class="highlightlink"]/text()').extract()

#//*[@id="maincontainer"]/table/tbody/tr[3]/td[1]/a

        return goldItem


#class S(Spider):
 #   rate = 1

  #  def __init__(self):
   #     self.download_delay = 1/float(self.rate)

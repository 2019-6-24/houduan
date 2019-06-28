# -*- coding: utf-8 -*-
import scrapy
from HousePrice.items import HousepriceItem

class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['wh.fang.lianjia.com/ershoufang/']
    start_urls = ['https://wh.lianjia.com/ershoufang/pg1/']

    def parse(self, response):
        size=response.css('.sellListContent')
        for each in size:
            item=HousepriceItem()
            xiaoqu=each.css('.address a::text').extract()
            louceng=each.css('.positionInfo::text').re('(\d+)层')
            price=each.css('.totalPrice span::text').extract()
            avg_price= each.css('.unitPrice span::text').re('(\d+)')
            area=each.css('.houseInfo::text').re('\d室\d厅')
            huxing=each.css('.houseInfo::text').re('(\d+平米)')
            item['xiaoqu']=xiaoqu
            item['louceng']=louceng
            item['price']=price
            item['avg_price']=avg_price
            item['area']=area
            item['huxing']=huxing
            yield item


        # items=[]
        # item = HousepriceItem()
        # xiaoqu = 'bsdnb'
        # louceng = 'vvv'
        # price = 242
        # avg_price = 24
        #
        # item['xiaoqu'] = xiaoqu
        # item['louceng'] = louceng
        # item['price'] = price
        # item['avg_price'] = avg_price
        # items.append(item)
        # return items

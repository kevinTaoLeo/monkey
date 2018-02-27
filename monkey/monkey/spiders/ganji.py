# -*- coding: utf-8 -*-
import scrapy
from ..items import MonkeyItem
class GanjiSpider(scrapy.Spider):
    name = 'ganji'
    allowed_domains = ['ganji.com']
    baseurl = 'http://sh.ganji.com/fang/agent/o'
    offset = 1
    start_urls = [baseurl+str(offset)]

    def parse(self, response):
        items = []
        res_list = response.xpath('//*[@id="puid-2736139587"]')
        for sel in res_list:
            item = MonkeyItem()
            item['tel'] = sel.xpath('.//div[4]/p/text()').extract()
            item['name'] = sel.xpath('.//div[2]/a/text()').extract()
            items.append(item)
            yield item
            print(item['tel'], item['name'])
#            print tel , name
#            for x in  item['name']:
#                print x.encode('utf-8')
            if len(response.xpath("//a[@class='next']")):
                url = response.xpath("//a[@class='next']/@href").extract()[0]
                yield scrapy.Request("http://sh.ganji.com/" + url, callback=self.parse)

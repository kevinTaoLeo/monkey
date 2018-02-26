# -*- coding: utf-8 -*-
import scrapy


class GanjiSpider(scrapy.Spider):
    name = 'ganji'
    allowed_domains = ['ganji.com']
    start_urls = ['http://sh.ganji.com/fang/agent/']

    def parse(self, response):
        res_list = response.xpath('//*[@id="puid-2736139587"]')
        for sel in res_list:
            tel = sel.xpath('.//div[4]/p/text()').extract()
            name = sel.xpath('.//div[2]/a/text()').extract()
            print tel , name
            for x in  name:
                print x.encode('utf-8')

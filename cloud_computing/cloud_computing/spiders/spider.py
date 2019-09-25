# -*- coding: UTF-8 -*-
# Created by thpffcj on 2019/9/24.

import scrapy
from cloud_computing.items import DoubanItem


class DoubanmovieSpider(scrapy.Spider):
    name = "doubanmovie"
    allowed_domains = ["movie.douban.com"]
    offset = 0
    url = "https://movie.douban.com/top250?start="
    start_urls = (
        url + str(offset),
    )

    def parse(self, response):
        item = DoubanItem()
        movies = response.xpath('//div[@class="info"]')
        for each in movies:
            # 电影名
            item['title'] = each.xpath('.//span[@class="title"][1]/text()').extract()[0]
            # 基本信息
            item['bd'] = each.xpath('.//div[@class="bd"]/p/text()').extract()[0]
            # 评分
            item['star'] = each.xpath('.//div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
            # 简介
            quote = each.xpath('.//p[@class="quote"]/span/text()').extract()
            if len(quote) != 0:
                item['quote'] = quote[0]
            yield item

        if self.offset < 225:
            self.offset += 25
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse)
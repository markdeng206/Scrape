# -*- coding: utf-8 -*-
from datetime import datetime
from scrapy import Spider, Request
import re
import json
import dateparser
import pytz
from spider.book.items import BookItem, PersonItem

class DoubanSpider(Spider):
    name = 'douban'
    allowed_domains = ['book.douban.com']
    start_urls = ['https://book.douban.com/']
    
    def parse(self, response):
        person_item = PersonItem({
            'id': 997810,
            'name': '卡勒德·胡赛尼'
        })
        yield BookItem({
            'id': 1770782,
            'name': '追风筝的人',
            'page_number': 362,
            'introduction': '12岁的阿富汗富家少爷阿米尔与仆人哈桑情同手足。然而，在一场风筝比赛后，发生了一件悲惨不堪的事，阿米尔为自己的懦弱感到自责和痛苦，逼走了哈桑，不久，自己也跟随父亲逃往美国。成年后的阿米尔始终无法原谅自己当年对哈桑的背叛。为了赎罪，阿米尔再度踏上暌违二十多年的故乡，希望能为不幸的好友尽最后一点心力，却发现一个惊天谎言，儿时的噩梦再度重演，阿米尔该如何抉择？故事如此残忍而又美丽，作者以温暖细腻的笔法勾勒人性的本质与救赎，读来令人荡气回肠。'
        })

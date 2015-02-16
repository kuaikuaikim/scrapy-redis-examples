import re
import json


from scrapy.selector import Selector
try:
    from scrapy.spider import Spider
except:
    from scrapy.spider import BaseSpider as Spider
from scrapy.utils.response import get_base_url
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle


from hrtencent.items import *
from misc.log import *


class HrtencentSpider(CrawlSpider):
    name = "hrtencent"
    allowed_domains = ["dewen.io"]
    start_urls = [
        "http://www.dewen.io/questions?page=%d" % d for d in range(1, 10, 1)
    ]
    rules = [
        Rule(sle(allow=("/q/\d*")), callback='parse_2'),
        Rule(sle(allow=("/questions?page=\d{,4}")), follow=True, callback='parse_1')
    ]

    def parse_2(self, response):
        items = []
        item = PositionDetailItem()
        sel = Selector(response)
        site = sel.css('.container')        
        item['sharetitle'] = site.css('#title::text').extract()
        item['description'] = site.css('#qst_content').extract()
        #item['duty'] = site.css('.c .l2::text').extract()
        item['link'] = response.url
        item['tags'] = site.css('#topic a::text').extract()
        
        #get content images url
        images_1 = sel.css('#qst_content img::attr(loadsrc)').extract()
        images_2 = sel.css('.post_area img::attr(loadsrc)').extract()
        item['image_urls'] = images_1 + images_2

        answers = []

        an_articles = site.css('.ans_item')
        for an_article in an_articles:
            answer = {}
            answer['description'] = an_article.css('.post_area').extract()
            answer['votes'] = an_article.css('.voting::attr(score)').extract()
            if an_article.css('.best_ans_text').extract():
                answer['chosen'] = 1
            else:
                answer['chosen'] = 0
            answers.append(answer)

        #item['answers'] = answers

        item['answers'] = answers

        items.append(item)

        print repr(item).decode("unicode-escape") + '\n'
        # info('parsed ' + str(response))
        self.parse_1(response)
        return items

    def parse_1(self, response):
        # url cannot encode to Chinese easily.. XXX
        info('parsed ' + str(response))

    def _process_request(self, request):
        info('process ' + str(request))
        return request

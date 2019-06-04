# -*- coding: utf-8 -*-
import scrapy
from cnvd_spider.items import CnvdSpiderItem
import re
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import time
import random


class ExampleSpider(CrawlSpider):
    name = "myspider"
    allowed_domains = ["www.cnvd.org.cn"]
    start_urls = ['http://www.cnvd.org.cn/flaw/list.htm?max=20&offset=20']
    rules = (
        Rule(LinkExtractor(allow=r"/flaw/show/*", unique=True),
             callback="parse_news", follow=True),
    )

    def printcn(uni):
        for i in uni:
            print(uni.encode('utf-8'))

    def parse_news(self, response):
        item = CnvdSpiderItem()
        # time.sleep(random.randint(1, 2))
        self.get_url(response, item)
        self.get_name(response, item)
        self.get_id(response, item)
        self.get_date(response, item)
        self.get_level(response, item)
        self.get_products(response, item)

        self.get_cve_id(response, item)
        self.get_detail(response, item)
        self.get_types(response, item)
        self.get_refer_url(response, item)
        self.get_method(response, item)
        return item

    def get_url(self, response, item):
        url = response.url
        if url:
            item['cnvd_url'] = url

    def get_name(self, response, item):
        name = response.xpath(
            # "//div[@class='blkContainerSblk']//h1/text()").extract()
            "//h1/text()").extract()
        print("\n======="+str(name)+"================\n")
        if name:
            item['cnvd_name'] = name[0].strip()

    # 1

    def get_id(self, response, item):
        iid = response.xpath(
            "//table[@class='gg_detail']//tr[td[1]='CNVD-ID']/td[2]/text()").extract()
        if iid:
            item['cnvd_id'] = iid[0].strip()

    # 2

    def get_date(self, response, item):
        date = response.xpath(
            "//table[@class='gg_detail']//tr[td[1]='公开日期']/td[2]/text()").extract()
        if date:
            item['cnvd_date'] = date[0].strip()

    # 3

    def get_level(self, response, item):
        item["cnvd_level"] = response.xpath(
            "//td[text()='危害级别']/following-sibling::td[1]//text()").extract()
        if item["cnvd_level"]:
            item["cnvd_level"] = "".join(
                [i.replace("(", "").replace(")", "").strip() for i in item["cnvd_level"]])
        else:
            item["cnvd_level"] = 'Null'

    # 4

    def get_products(self, response, item):
        products = response.xpath(
            "//table[@class='gg_detail']//tr[td[1]='影响产品']/td[2]/text()").extract()
        if products:
            item['cnvd_products'] = products[0].strip()

    # 5

    def get_cve_id(self, response, item):
        try:
            cve_id = response.xpath(
                "//table[@class='gg_detail']//tr[td[1]='CVE ID']/td[2]//text()").extract()
            if cve_id:
                temp = ''
                for i in range(len(cve_id)):
                    temp += cve_id[i].strip()
                item['cnvd_cve_id'] = temp
        except:
            item['cnvd_cve_id'] = ''

    # 6

    def get_detail(self, response, item):

        detail = response.xpath(
            "//table[@class='gg_detail']//tr[td[1]='漏洞描述']/td[2]//text()").extract()

        if detail:
            temp = ''
            for i in range(len(detail)):
                temp += detail[i].strip()
            item['cnvd_detail'] = temp
    # 7

    def get_types(self, response, item):

        types = response.xpath(
            "//table[@class='gg_detail']//tr[td[1]='漏洞类型']/td[2]/text()").extract()

        if types:
            item['cnvd_types'] = types[0].strip()

    # 8
    def get_refer_url(self, response, item):

        refer_url = response.xpath(
            "//table[@class='gg_detail']//tr[td[1]='参考链接']/td[2]//text()").extract()

        if refer_url:
            temp = ''
            for i in range(len(refer_url)):
                temp += refer_url[i].strip()
            item['cnvd_refer_url'] = temp

    # 9

    def get_method(self, response, item):

        method = response.xpath(
            "//table[@class='gg_detail']//tr[td[1]='漏洞解决方案']/td[2]/text()").extract()

        if method:
            item['cnvd_method'] = ''
            for i in range(len(method)):
                item['cnvd_method'] += method[i].strip()

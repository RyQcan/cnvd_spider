# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CnvdSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # url
    cnvd_url = scrapy.Field()
    # 名称
    cnvd_name = scrapy.Field()
    # cnvd-id
    cnvd_id = scrapy.Field()
    # 公开日期
    cnvd_date = scrapy.Field()
    # 危害级别
    cnvd_level = scrapy.Field()
    # 影响产品
    cnvd_products = scrapy.Field()
    # cve-id
    cnvd_cve_id = scrapy.Field()
    # 漏洞描述
    cnvd_detail = scrapy.Field()
    # 漏洞类型
    cnvd_types = scrapy.Field()
    # 参考链接
    cnvd_refer_url = scrapy.Field()
    # 解决方案
    cnvd_method = scrapy.Field()

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, TEXT, Index, DATE
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
import re
import csv
import codecs

engine = create_engine(
    "mysql+pymysql://root:root@localhost/scrapy?charset=utf8", max_overflow=5)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Cnvdtable(Base):
    __tablename__ = 'cnvd_table'

    cnvd_id = Column(String(32), primary_key=True)
    cnvd_url = Column(String(64))
    cnvd_date = Column(DATE)
    cnvd_level = Column(String(64))
    cnvd_cve_id = Column(String(32))

    cnvd_name = Column(String(512))
    cnvd_products = Column(TEXT)
    cnvd_detail = Column(TEXT)
    cnvd_types = Column(String(32))
    cnvd_refer_url = Column(String(512))
    cnvd_method = Column(String(512))

    __table_args__ = (
        Index('cnvd_id', 'cnvd_url'),
    )


Base.metadata.create_all(engine)


class CnvdSpiderPipeline(object):
    def process_item(self, item, spider):
        return item


class CnvdSpiderInfoPipeline(object):
    def open_spider(self, spider):
        # a
        self.f = open('cnvd.csv', 'w')

    def close_spider(self, spider):
        self.f.close()

    def process_item(self, item, spider):
        try:
            writer = csv.writer(self.f, codecs.BOM_UTF8)
            c = []
            for i in item.values():
                c.append(i)
            writer.writerow(c)
            # item = itemt(item)
            obc = Cnvdtable(
                cnvd_id=item['cnvd_id'],
                cnvd_url=item['cnvd_url'],
                cnvd_date=item['cnvd_date'],
                cnvd_level=item['cnvd_level'],
                cnvd_cve_id=item['cnvd_cve_id'],

                cnvd_name=item['cnvd_name'],
                cnvd_products=item['cnvd_products'],
                cnvd_detail=item['cnvd_detail'],
                cnvd_types=item['cnvd_types'],
                cnvd_refer_url=item['cnvd_refer_url'],
                cnvd_method=item['cnvd_method'],
            )
            session.add(obc)
            session.commit()
            print("\n"+item['cnvd_name']+" ==============存储成功\n")
        except BaseException as e:
            print(e)
        return item

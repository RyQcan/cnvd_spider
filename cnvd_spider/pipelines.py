# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, TEXT, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
import re

engine = create_engine(
    "mysql+pymysql://root:root@localhost/scrapy?charset=utf8", max_overflow=5)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Cnvdtable(Base):
    __tablename__ = 'cnvd_table'

    id = Column(Integer, primary_key=True)
    cnvd_url = Column(String(64))
    cnvd_name = Column(String(64))
    cnvd_id = Column(String(32))
    cnvd_date = Column(String(32))
    cnvd_level = Column(String(32))
    cnvd_products = Column(String(64))
    cnvd_cve_id = Column(String(32))
    cnvd_detail = Column(TEXT)
    cnvd_types = Column(String(32))
    cnvd_refer_url = Column(String(64))
    cnvd_method = Column(String(64))

    __table_args__ = (
        # UniqueConstraint('id', 'news_title', name='uix_id_name'),
        Index('cnvd_url', 'cnvd_id'),
    )


Base.metadata.create_all(engine)
session.execute('alter table learn_newstable convert to character set gbk')


class CnvdSpiderPipeline(object):
    def process_item(self, item, spider):
        return item


class CnvdSpiderInfoPipeline(object):
    def open_spider(self, spider):
        self.f = open('CnvdSpiderInfo.txt', 'w')

    def close_spider(self, spider):
        self.f.close()

    def process_item(self, item, spider):
        try:
            line = str(dict(item)) + '\n'
            self.f.write(line)
            dic = dict(item)
            obc = Cnvdtable(
                cnvd_url=dic['cnvd_url'],
                cnvd_name=dic['cnvd_name'],
                cnvd_id=dic['cnvd_id'],
                cnvd_date=dic['cnvd_date'],
                cnvd_level=dic['cnvd_level'],
                cnvd_products=dic['cnvd_products'],
                cnvd_cve_id=dic['cnvd_cve_id'],
                cnvd_detail=dic['cnvd_detail'],
                cnvd_types=dic['cnvd_types'],
                cnvd_refer_url=dic['cnvd_refer_url'],
                cnvd_method=dic['cnvd_method'],
            )
            session.add(obc)
            session.commit()
        except:
            pass
        return item

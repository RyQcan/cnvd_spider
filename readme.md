# 爬取cnvd最近3年的漏洞详情

## 环境

软件 |版本 
 -|-
 python|3.6
 scrapy|
 sqlalchemy|
 mysql|5.7

`sudo python3 -m pip install --upgrade pip`

`sudo python3 -m pip install --upgrade setuptools`

`sudo python3 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ scrapy`

`sudo python3 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ sqlalchemy`

## 运行

`python3 main.py`


## 功能

爬取CNVD漏洞详情,sqlalchemy存库,并写入csv文件

## 使用前须知

* 修改User-Agent
* 修改数据库连接语句

## 避坑

之前尝试好多次都是爬取8个页面后返回的内容变空,网上查了一下,原来是cnvd的cookie反爬虫机制导致的,看网上大家的办法都是用selenium,后来发现只需要在settings.py里,把cookie disable就能反反爬,原理就是每次都相当于新请求,完美
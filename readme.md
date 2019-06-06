# 爬取cnvd最近3年的漏洞详情

## 环境

软件 |版本 
 -|-
 python|3.6
 scrapy|
 sqlalchemy|
 selenium|
 mysql|5.7

`sudo python3 -m pip install --upgrade pip`

`sudo python3 -m pip install --upgrade setuptools`

`sudo python3 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ scrapy`

`sudo python3 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ sqlalchemy`

## 运行

`python3 main.py`


## 功能

* 按顺序依次爬取cnvd的漏洞详情,起始url在代码中修改

* 使用sqlchemy保存数据,也可以改为csv文件存储

## 使用前须知

* 修改User-Agent
* 修改数据库连接语句

## 避坑

未完成
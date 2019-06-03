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
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

* 修改User-Agent 必须与你本地的chrome一样

* 修改数据库连接语句

* /scrapy/downloadermiddelwares/cookies.py 修改为

```python
 def process_request(self, request, spider):
        cookiejarkey = request.meta.get("cookiejar")
        jar = self.jars[cookiejarkey]

        if request.meta.get('dont_merge_cookies', False):
            jar = CookieJar()

        cookies = self._get_request_cookies(jar, request)
        for cookie in cookies:
            jar.set_cookie_if_ok(cookie, request)

        # set Cookie header
        request.headers.pop('Cookie', None)
        jar.add_cookie_header(request)
        self._debug_cookie(request, spider)
```

## 避坑

scrapy官方有坑,,dont_merge_cookies 开启后实际功能是不发送cookies,所以需要修改官方代码/scrapy/downloadermiddelwares/cookies.py
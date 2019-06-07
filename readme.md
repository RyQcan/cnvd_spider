# 爬取cnvd最近3年的漏洞详情

## 环境

| 软件                 | 版本                              |
| -------------------- | --------------------------------- |
| python               | 3.6                               |
| mysql                | 5.7                               |
| google-chrome-stable | 建议添加google官方仓库然后apt安装 |
| chromedriver         | 与chrome版本一致                  |

| python库   | 版本   |
| ---------- | ------ |
| scrapy     | latest |
| sqlalchemy | latest |
| selenium   | latest |

安装出错时请先升级pip

`sudo python3 -m pip install --upgrade pip`

`sudo python3 -m pip install --upgrade setuptools`

## 功能

* 按爬取cnvd的漏洞详情,起始url在代码中修改

* 使用sqlchemy保存数据,也可以改为csv文件存储

* 使用selenium打开浏览器获取cookie,每7次请求更新cookie

## 使用前须知

* 修改User-Agent 必须与你本地的chrome一样

* 修改数据库连接语句

* python包:scrapy/downloadermiddelwares/cookies.py 修改为

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

## 运行

`sudo python3 main.py`

## 避坑

scrapy官方有坑,,dont_merge_cookies 开启后实际功能是不发送cookies,所以需要修改官方代码/scrapy/downloadermiddelwares/cookies.py
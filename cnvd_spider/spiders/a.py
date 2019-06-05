# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import ast

def COOKIES():
    chrome_options = Options()
    # 加上下面两行，解决报错
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("http://www.cnvd.org.cn/flaw/show/CNVD-2017-27958")
    cj = driver.get_cookies()
    cookie = ''
    for c in cj:
        # if (c==cj[-1]):
        #     cookie += "'"+c['name'] + "':'" + c['value'] + "'"
        # else:
        cookie += "'"+c['name'] + "':'" + c['value'] + "',"
    cookie=ast.literal_eval('{'+cookie+'}')
    return cookie
    driver.quit()


print(COOKIES())

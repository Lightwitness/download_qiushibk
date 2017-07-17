#!E:\Python python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/17 17:08
# @Author  : Lightwitness
# @File    : qiushibk.py
# @Software: PyCharm

import requests
from lxml import etree
import os
for pageindex  in range(36):
    url = 'https://www.qiushibaike.com/text/page/' + str(pageindex) + '/'
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
    headers = {'User-Agent': user_agent}

    html = requests.get(url, headers=headers, timeout=10)

    selector = etree.HTML(html.text)

    selectart = selector.xpath('//*[@id="content-left"]/div/a[1]/div[1]/span/text()')

    for art in selectart:
        art1 = art.encode('utf-8')
        with open('./duanzi.txt', 'a') as f:
            f.write(art1 + '\n')
            print '保存成功'


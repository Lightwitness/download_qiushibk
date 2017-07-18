#!E:\Python python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/18 16:13
# @Author  : Lightwitness
# @File    : newbk.py
# @Software: PyCharm




import json
import requests
from lxml import etree

class duanzi ():
    def __init__(self):
        pass
    def get_list (self , url):
        self.url  = url
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
        headers = {'User-Agent': user_agent}
        request = requests.get(url , headers = headers , verify = False)

        if request.status_code != 200:
            print request.status_code

        selector = etree . HTML( request.text)
        selectdivs = selector.xpath ('//*[@id="content-left"]/div')

        for div in selectdivs:
            duanzi  = {}
            article = div.xpath('a[@class="contentHerf"]/div/span/text()')

            name = div.xpath('div[@class="author clearfix"]/a[2]/h2/text()')

            gender = div.xpath('div[@class="author clearfix"]/div/@class')

            age = div.xpath('div[@class="author clearfix"]/div/text()')

            great = div.xpath('div[@class="stats"]/span/i/text()')

            comment = div.xpath('div[@class="stats"]/span[2]/a/i/text()')

            if article:
                duanzi ['content'] = article[0].strip()
            if name:
                duanzi ['name'] = name[0].strip()
            if gender:
                duanzi['gender'] = gender[0].strip()
            if age:
                duanzi['age'] = age[0].strip()
            if great:
                duanzi['great'] = great[0].strip()
            if comment:
                duanzi['comment'] = comment[0].strip()

            self.write_fp(duanzi)

    def write_fp(self,item):

        jStr = json.dumps(item, ensure_ascii=False)
        str = jStr.encode('Utf-8')

        with open('./duanzi.json', 'a') as f:
            f.write(str + '\n')
            print '保存成功'




    def run(self):
        for pageindex in range(36):
            url = 'https://www.qiushibaike.com/text/page/' + str(pageindex) + '/'
            self.get_list(url)

if __name__ == '__main__':
    duanzi1 = duanzi()
    duanzi1.run()





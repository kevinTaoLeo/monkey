#!/usr/bin/env python

import re
import urllib

user = r'<a class="broker-name" href="/fang_(.+?)/" target="_blank">(.+?)</a>'
iphone = r'<p class="tel">(.+?)</p>'
pageNum = 10
getNum = 5

def getHtml(url):
    return urllib.urlopen(url).read()

def splitHtml(regex, html):
    return re.compile(regex).findall(html)

def getInfo(html):
    iphone_list = splitHtml(iphone, html)
    user_list = [u[1] for u in splitHtml(user, html)]
    for index in range(pageNum):
        print '%s - %s' % (user_list[index], iphone_list[index])

for i in range(1,getNum):
    html = getHtml("http://sh.ganji.com/fang/agent/o%s/" % i)
    getInfo(html)
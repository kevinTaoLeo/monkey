#!/usr/bin/env python
#coding:utf-8

import requests

response = requests.get('http://www.baidu.com')
print(type(response))
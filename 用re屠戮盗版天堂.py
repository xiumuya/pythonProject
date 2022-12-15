# coding:utf-8
import time

import  requests
import re
import urllib3
from timeit import timeit

urllib3.disable_warnings()
url='https://www.dy2018.com/'
resp=requests.get(url,verify=False)
resp.encoding=resp.apparent_encoding
resp.raise_for_status()
page_content=resp.text
object=re.compile(r'<li><a href=\'(?P<net>.*?)\''
                  r'.*?title="(?P<name>.*?)"',re.DOTALL)
result=object.finditer(page_content)
for it in result:
    with open('some_movies.txt', 'a', encoding='utf-8') as f:
        print(it.group('net'))
        print(it.group('name'),file=f)
        time.sleep(0.2)
        newurl= url +it.group('net')
        resp1=requests.get(newurl,verify=False)
        resp1.encoding=resp1.apparent_encoding
        page_content1=resp1.text
        object1=re.compile(r'<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<xl>.*?)">',re.DOTALL)
        time.sleep(0.3)
        result1=object1.finditer(page_content1)
        for it1 in result1:
            print(it1.group('xl'),file=f)
        resp1.close()
resp.close()
print('over')


# coding:utf-8
import sys
import time
from lxml import etree
import requests
import re
import  random
# key_word=input('please enter a key word')
user_agent_list = ["Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/61.0",
                    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
                    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
                    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
                    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
                    ]
headers = {'User-Agent': random.choice(user_agent_list),'Connection':'close'}
        # print(line)
x=0
with open('abc.txt','r')as f:
    for l in f:
        line=l.rstrip('\n')
        r1=requests.get(line,headers=headers,verify=False)
        import urllib3
        urllib3.disable_warnings()
        requests.adapters.DEFAULT_RETRIES = 5
        r1.encoding=r1.apparent_encoding
        r1.raise_for_status()
        r1.close()
        time.sleep(5)
        tree=etree.HTML(r1.text)
        lst=tree.xpath('//ul/li/div/a/img/@data-echo')
        with open('net.txt','a')as f1:
            for i in lst:
                f1.write(i+'\n')


# with open('net.txt',mode='r') as f:
#     for line in f:
#         try:
#             x+=1
#             if x%50==0:
#                 time.sleep(60)
#             line=line.rstrip('\n')
#             r2=requests.get(line,headers=headers,verify=False)
#             imgq=line.split('/')[-1]
#     #     r2=requests.get(l,headers)
#     #
#             time.sleep(3)
#             requests.adapters.DEFAULT_RETRIES = 5
#             r2.encoding=r2.apparent_encoding
#             r2.raise_for_status()
#             with open('E:\\scrapy_pic\{}'.format(imgq),'wb') as f:
#                 f.write(r2.content)
#                 r2.close()
#         except requests.ConnectionError:
#             r2.status_code='Connection refused'
#             print('error!')
print('over!')






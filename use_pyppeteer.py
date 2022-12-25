import asyncio
import re
import sys

import requests
from pyppeteer import launch

headers={'user_agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36 Edg/108.0.1462.54'}

async def main():
    browser = await launch(headless=False, executablePath=r'C:\Users\asus\AppData\Local\pyppeteer\pyppeteer\local-chromium\588429\chrome-win32\chrome.exe')  # 关闭无头浏览器

    page = await browser.newPage()
    await page.goto('https://pc.yiyouliao.com/msn/article.html?recId=aa708094f3304acfbf9d3278d3281f86_s&infoId=II0143OMBZVSHGG')  # 跳转

    # await page.screenshot({'path': 'example.png'})  # 截图
    # content=await page.evaluate('document.body.textContent',force_expr=True)
    content=await page.content()
    img_lst=re.finditer('img src="(?P<net>.*?)\?time',content)
    i=0
    for img in img_lst:
        i+=1
        with open('E:\scrapy_pic\page_{}.jpg'.format(i),'wb')as  f:
            r=requests.get(img.group('net'),headers)
            f.write(r.content)
            if i==6:
                sys.exit()
    await browser.close()  # 关闭

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
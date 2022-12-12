import pandas as pd
from bs4 import BeautifulSoup
import requests
import random
from urllib.error import HTTPError,URLError
url='https://www.shanghairanking.cn/rankings/bcur/202211.html'
user_agent_list = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/61.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
    ]
headers={
         'User-Agent':random.choice(user_agent_list)
}
def get_text(url,headers):
    try:
        r = requests.get(url, headers, timeout=10)
        # r.raise_for_status()
        r.encoding = r.apparent_encoding
        bs = BeautifulSoup(r.text, 'html.parser')
        global textlist, textlist2
        textlist = bs.find_all('td', attrs={'data-v-3fe7d390': ''})
        textlist2 = bs.find_all("a", {'class': "name-cn", 'data-v-b80b4d60': ""})
        r.close()
    except Exception as e:
        print(e)
get_text(url,headers)
# print(textlist2[0].string)
# print(len(textlist))
# print(textlist[1].string)
lst = []
lst1 = []
lst2 = []
lst3_school = []
for i in range(30):
    lst.append(textlist[6*i].string)
    lst1.append(textlist[6*i+4].string)
    lst2.append(textlist[6*i+5].string)
    lst3_school.append(textlist2[i].string)
lst_rank=[x.strip() for x in lst ]
lst1_score=[float(x.strip()) for x in lst1]
lst2_b=[float(x.strip())for x in lst2 if x.strip]
df=pd.DataFrame({'排名':lst_rank,'学校名称':lst3_school,"总分":lst1_score,'办学层次':lst2_b})
df.to_excel('df.xlsx',index=False)
print(df)

import  matplotlib.pyplot as plt
colors=['g','c','b','orange','r','m','y','pink','purple','silver']
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False
plt.figure(figsize=(15,10),dpi=300)
grid=plt.GridSpec(2,2)
plt.subplot(grid[0,:])
bar=plt.bar(x=lst3_school[:10],height=lst1_score[:10],color=colors,hatch='/')
plt.xticks(rotation=15)
# for i in range(10):
#     plt.text(lst3_school[i], lst1_score[i]*1.01, lst1_score[i])
plt.bar_label(bar)#目的与上相同
plt.title('中国前十大学评分')
plt.subplot(grid[1,:])
bar2=plt.bar(x=lst3_school[:10],height=lst2_b[:10],color=colors,hatch='/')
plt.bar_label(bar2)
plt.xticks(rotation=20)
plt.title('中国前十大学办学层次')
plt.tight_layout()
plt.savefig('pi.jpg')
plt.show()



# coding:utf-8
#author 35-牟惠洋
import matplotlib.pyplot as plt
#重庆
a1=15412#大专以上学历
a2=15956#高中（含中专）学历
a3=30582#初中学历
a4=29894#小学学历
a5=8156#文盲
edu_num=[a1,a2,a3,a4,a5]
#中文显示
plt.rcParams['font.sans-serif']='SimHei'
plt.rcParams['axes.unicode_minus']=False


label=["大专以上学历","高中（含中专）学历","初中学历","小学学历","文盲"]
explode=[0.0,0.0,0.01,0,0]
color=['r','g','c','b','m']
plt.figure(figsize=(12,8),dpi=150)
grid=plt.GridSpec(2,2)
plt.subplot(grid[0,:])

plt.pie(edu_num,labels=label,explode=explode,autopct='%.2f%%',colors=['c','orange','r','y','pink','silver'],startangle=90)#labels表示标签，explode表示各板块离开中心的距离，autopct标签饼图百分比设置，colors表示颜色，shadow表示阴影（增加立体感）
# plt.legend(loc='best',)
# plt.legend(loc='upper left')
# plt.legend(loc=(-0.6,0.6),)
plt.title('重庆每十万人中受教育的人数的程度')#设置标题
# plt.tight_layout()#调整多图被截断或遮挡等情况
# plt.show()

a1=15412#重庆
a2=13267#四川
a3=41980#北京
a4=33872#上海
a5=16990#浙江
a6=11601#云南
a7=10952#贵州
a8=11019#西藏
a=[a1,a2,a3,a4,a5,a6,a7,a8]
a9=sum(a)/len(a)
a.append(a9)
b=[x/1000 for x in a]
b_=['%.2f%%'%y for y in b]
print(b_)
city=['重庆','四川','北京','上海','浙江','云南','贵州','西藏','平均']
plt.rcParams['font.sans-serif']=['SimHei']#处理中文显现问题
plt.subplot(grid[1,:])
base_num=plt.bar(city,height=a,color=['c','orange','r','y','pink','silver'],)
edu_percent=plt.bar(city,height=b)
plt.plot(city,a,)
lst=[]
for x in range(len(city)):
    lst.append(a[8])
plt.plot(city,lst)
# method1
# for i in range(len(city)):
#     plt.text
#method2
plt.bar_label(base_num,)
# plt.bar_label(edu_percent)
for x in range(len(edu_percent)):
    plt.text(city[x],100*b[x],b_[x])
plt.xlabel('城市')#设置x轴标签
plt.ylabel('人数')#设置y轴标签
plt.title('每10万人口中高中以上学历的人数占比')#设置题目
# plt.legend(city,fontsize=10,ncol=8)
plt.tight_layout()
plt.savefig('demo.jpg')
plt.show()
# plt.boxplot(a)
# plt.title('每10万人口中高中以上学历的人数占比')#设置题目
# plt.xlabel('')
# plt.text(1,a[3]*1.01,city[3])
# plt.ylabel('人数')
# plt.show()

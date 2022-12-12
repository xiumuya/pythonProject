# coding: utf-8
import numpy as np
import matplotlib.pylab as plt
X = np.linspace(0.1,0.9,50)
def sigmoid(x):
    return 1-(1/1+np.exp(-x))
Y=0.3*sigmoid(X)
Z=0.7*sigmoid(X)
def func(X,Y):
    return (1-X)*Z/(X*Y+(1-X)*Z)
plt.figure(figsize=(15,10),dpi=300)
plt.plot(X, func(X,Y))
plt.ylim(-0.1, 1.1)
plt.xlabel('P(A)')
plt.ylabel('P(A~|B)')
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.title('某地区佩戴口罩的比例与感染是由于未佩戴口罩概率的关系',fontsize=6)
plt.savefig('pic.png')
plt.show()
print(X)
print(Y)
print(func(X,Y))


#开始思路:分开看，看分子，看分母，再整合起写
b=1
c=0
tmp=1
sum = 1
lst=[1]#第一个数是1
import  pyinputplus as pyip
a=pyip.inputNum('请输入一个大于2,小于3.1415925的数:\n',greaterThan=2,lessThan=3.1415925)#不想写if来判断
def func(x):#经典的递归
    if x==1:
        return 1
    else:
        return x*func(x-1)#从这里看到进行到一定次数，分子后面一定会很大很大
while float(a)> 2*sum:#注意循环终止条件，最后得到的数是第一个比它大的
    tmp+=2
    b=tmp*b
    c+=1
    sum=sum+func(c)/b
    lst.append(2*sum)
    #虽然会占用一点内存，但好用
print(lst)
print('第{}次'.format(c))
print("%.7f" %(lst[-2]))#每次取倒数第二个，即题目所求。

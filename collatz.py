# coding:utf-8
import pyinputplus as pyip
def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1
#2.让⽤户输⼊⼀个整数并不断调⽤这个collatz()，直到函数返回值为1
try:
    num = pyip.inputNum('enter a number:\n')
    while num != 1:
        num = collatz(num)
        print(num)
    if num==1:
        print()
except:
    print('Error!')
import numpy as np
a=np.arange(1,5,2)
print(a)
y=[]


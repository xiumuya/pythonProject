# coding:utf-8
#求最大的子序列,写出起始位置和终止位置，假设序列中的元素有正数
import random
import time
lst=[random.uniform(-1,1) for i in range(1000000)]#生成[-1,1]均匀分布的列表,绝大多数时候，列表中有大于0的数

# random.seed(0)
#method1
# sum_max=0
# a=0
# b=0
# start=time.perf_counter()
# for i in range(len(lst)):
#     sum=0
#     for k in range(i,len(lst)):
#         sum+=lst[k]
#         # if sum<0:减少不必要的计算
#         #     continue   反向优化，耗用的时间还多1s左右
#
#         if sum_max<sum:
#             sum_max=sum
#             a=i+1
#             b=k+1#自动更新,要最后一次
# end=time.perf_counter()
# print(sum_max)
# print('start:{} end:{} time:{}'.format(a,b,end-start))
# print('-----------------------')
#method2
end=time.perf_counter()

sum1=0
sum_max1=0
q=0
for i in range(len(lst)):
    sum1+=lst[i]
    if sum1 < 0:
        sum1 = 0

    if sum_max1<sum1:
        sum_max1 = sum1
        q=i

sum2=0
sum_max2=0
p=0

for j in range(1,len(lst)+1):
    sum2 += lst[-j]
    if sum2 < 0:
        sum2 = 0

    if sum_max2 < sum2:
        sum_max2 = sum2
        p = j




end2=time.perf_counter()
print(sum_max1)
print("start:",len(lst)-p+1,'end:',q+1,'time:',end2-end)

# method3
def linear_find_max_subarray(array):
    '''
    线性时间复杂度查找最大子数组
    '''
    left = 0
    right = 0
    i = left
    j = right
    max_sum = 0
    sum_now = 0
    while j < len(array):
        sum_now += array[j]
        if sum_now > max_sum:  # 元素和增大，调整相关变量记录当前元素构成的子数组
            max_sum = sum_now
            left = i
            right = j
        if sum_now < 0:  # 如果元素和小于0，那么[i:j]就不属于最大子数组的一部分
            sum_now = 0
            i = j + 1
        j += 1
    return left+1,right+1, max_sum
print(linear_find_max_subarray(lst))

# method4
sum1=0
# print(lst)
sum_max1=0
p=0
q=0
left=p

for right in range(len(lst)):
    sum1+=lst[right]
    if sum1 < 0:
        sum1 = 0
        left=right+1
    if sum_max1<sum1:
        sum_max1 = sum1
        p=left
        q=right
print(p+1,q+1,sum_max1)






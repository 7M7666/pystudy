#洋们车问题
from random import *
a=0
b=0
c=0
for i in range(10000):
    a=randint(1,3)
    b=randint(1,3)
    if a==b:
        c+=1
c=c/10000    
print ("不换的概率是{}".format(c))
c=0
for i in range(10000):
    a=randint(1,3)
    b=randint(1,3)
    if a==b:
        c+=1
        continue #continue的作用是继续循环 不执行下面的语句
    while(a!=b):
        d=randint(1,3)
        if d!=a and d!=b:
            break #筛选出不是车也不是参赛者猜的门
    e=a,d
    b=choice(e) #这代表参赛者在车和另一只羊里面选 choice的作用是随机返回e中的一个值
    if a==b:
        c+=1
c=c/10000
print ("换的概率是{}".format(c))
#随机生成random库
from random import *
a=randint(0,100)
print("随机生成一个0-100的数a:",a)
b=randrange(1,100,2)
print("随机生成一个0-100的奇数b:",b)
c="abcdefghjk"
d=sample(c,4)
print("随机生成返回四个字符",d)
e=["i","m","big","pig"]
q=choice(e)
print("随机返回一个字符串",q)
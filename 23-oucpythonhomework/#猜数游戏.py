#猜数游戏
from random import *
a=randint(0,100)
b=eval(input("请输入你猜的数"))
cnt=0
while a!=b:
    if a<b:
        print("你猜的数太大了！")
        cnt+=1
    else:
        print("你猜的数太小了！")
        cnt+=1
    b=eval(input("请输入你猜的数"))

print("ok你终于猜对了你用了:{:}次".format(cnt+1))  
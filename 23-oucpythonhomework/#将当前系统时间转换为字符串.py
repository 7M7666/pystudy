#将当前系统时间转换为字符串
from datetime import *
a=datetime.now()
b=str(a)
print(b)
#用datetime库输出五种不同的日期格式
someday=datetime(2024,4,22,0,0,0,0)
someday.strftime("%Y-%m-%d %H:%M:%S")
print(someday)
#用datetime库对一个程序运行计时
s=datetime.now()
import time
time.sleep(1)
e=datetime.now()
r=e-s
print(r) 
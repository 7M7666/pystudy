import time 
a=50
print("执行开始".center(a//2,'-'))
for i in range(a+1):
    q="*"*i
    b="."*i
    c=(i/a)*100
   
    print("\r{:^3.of}%[{}->{}]".format(c,q,b),\
        end="")
    time.sleep(0.5)


#程序的异常处理
#try except语句
try:
    num=eval(input("请输入一个整数"))
    print(num**2)
except NameError:
    print("请输入一个整数！！")
#异常的高级用法和elif相似 finally 是无论如何都要进行

    
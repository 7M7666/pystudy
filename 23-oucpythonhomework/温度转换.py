#目的为实现华氏度和摄氏度的转化
#转化规则：华氏度=摄氏度*1.8+32
print("please choose c or f\n")
wendu=input("c or f")
if wendu[-1]in['f'or 'F']:
    #wendu【-1】表示的是输入的字符中的最后一个字符
    c=(eval(wendu[0:-1])-32)/1.8

    #eval函数表达的是把字符串中的表达式转换为数字表达式
    #ex：a=1 b=2 c=eval("a+b") print (c) 输出结果就是3
     #此时为摄氏度
    print(c)
elif wendu[-1]in['c'or 'C']:
    f=eval(wendu[0:-1])*1.8+32
    #此时为华氏度
    print(f)
else:print("error")
# 异常案例

try:
    mun = int(input("请输入一个数字："))
    rst = 100/mun
    print("计算结果是：{0}".format(rst))

# 如果多种情况error，需要把越具体的错误，越往前放
# 在异常类关系中，越是子类异常，越要往前放
# 越是父类越往后放
# 在处理异常的时候，一旦拦截到某个异常，则不在继续往下查看，直接进行下一个
# 如果有finally则执行finally语句，否则执行下一个大的语句
except ZeroDivisionError as e:
    print("你输入的是啥？？？？")
    print(e)
    # exit是退出程序
    exit()
except NameError as e:
    print("名字错了")
    print(e)
    exit()

# 所有异常都是继承自Exception
# 如果选择Exception,任何异常都会被拦截
# Exception一般都是放在最后一个异常使用
except Exception as e:
    print("反正就是有错，你在想想？？？")


print("ksjkajsakhjjj")
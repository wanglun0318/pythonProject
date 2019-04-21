# 引入随机模块random
import random


print("大家好,我们来玩一个游戏......")
print("=======心有灵犀==========")
print("这是一个猜数字的游戏，看看你能不能猜出我心里的数字！！！")
# 生成一个随机数
secret = random.randint(0,10)
temp = input("请输入你猜的数字:")
# isis = isinstance(temp,int)

guess = int(temp)

while  guess != secret:
    temp = input("没猜对哦，继续再猜猜:")
    guess = int(temp)
    if guess == secret:
        print("恭喜你猜对了，看来咱俩真是心有灵犀！！！")
        print("=================游戏结束===================")
        exit()
    else:
        if guess > secret:
            print("哟，大了一点哦，马上就要猜对了......")
            print("====================================")
        else:
            print("哟，小了一点哦，马上要猜对了......")
            print("====================================")


print("哟，一下就猜中了，真是心有灵犀一点通啊！")
print("=================游戏结束===================")
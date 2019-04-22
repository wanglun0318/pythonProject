# 注册新用户
def new_user():
    username = input("请输入用户名：")
    while username in accounts:
        username = input("此用户名已经被使用请重新输入：")
    else:
        accounts[username] = input("请输入你的密码：")

    print("注册成功，赶紧试试登录吧！")

# 用户登录
def old_user():
    username = input("请输入用户名：")

    while username not in accounts:

        print("您输入的帐号或者密码错误！")
        username = input("请输入用户名：")

    else:

        password = input("请输入你的密码：")
        while password != accounts[username]:

            print("您输入的帐号或者密码错误！")
            password = input("请输入你的密码：")
        else:

            print("欢迎登录XXOO系统！！！")


print("|--- 新建用户：N/n ---|")
print("|--- 登录帐号：E/e ---|")
print("|--- 退出程序：Q/q ---|")
contacts = input("|--- 请输入指令代码：")

accounts = dict()
while contacts not in "NnEeQq":
    contacts = input("您输入的指令错误，请重新输入：")
else:
    while contacts not in "Qq":
        if contacts == "N" or contacts == "n":
            new_user()
            print(accounts)
            contacts = input("如您还想其他操作，请重新输入指令：")
        elif contacts == "E" or contacts == "e":
            old_user()
            contacts = input("如您还想其他操作，请重新输入指令：")
    else:
        print("再见！真想下次早点见到你呢！！！")
        exit()
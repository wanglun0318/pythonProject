print("|--- 欢迎进入通讯路程序 ---|")
print("|--- 1：查询联系人资料  ---|")
print("|--- 2：插入新的联系人  ---|")
print("|--- 3：删除已有联系人  ---|")
print("|--- 4：退出通讯录程序  ---|")

contacts = dict()
instruct = int(input("请输入相关指令代码："))


def con(instruct):
    if instruct == 1:
        print(contacts)
        print(type(contacts))
        a = int(input("请输入相关指令代码："))
        return a
    elif instruct == 2:
        conkey = input("请输入联系人姓名：")
        if conkey in contacts:
            print("您输入的联系人已经存在，")
            if input("是否修改电话号码（YES/NO):") == "YES":
                contacts[conkey] = input("请输入用户联系电话")
        else:
            contacts[conkey] = input("请输入用户联系电话")
        print(contacts)
        a = int(input("请输入相关指令代码："))
        return a
    elif instruct == 3:
        conkey = input("请输入要删除的联系人姓名：")
        del contacts[conkey]
        print(contacts)
        a = int(input("请输入相关指令代码："))
        return a
    elif instruct == 4:
        print("|--- 感谢使用通讯录  ---|")
        exit()
    else:
        print("输入有误，程序关闭！！！！")
        exit()


instruct = con(instruct)

while instruct != 4:
    instruct = con(instruct)
else:
    print("|--- 感谢使用通讯录  ---|")
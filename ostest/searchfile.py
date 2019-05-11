import os   # 文件搜索


def search_file(start_dir, target):
    os.chdir(start_dir)  # 改变工作目录

    for each_file in os.listdir(os.curdir):
        if each_file == target:
            print(os.getcwd() + os.sep + each_file)  # 使用os.sep使程序更标准
        if os.path.isdir(each_file):
            search_file(each_file, target)  # 递归调用
            os.chdir(os.pardir)  # 递归调用后切记返回上一层目录


start_dir = input("请输入待查找的初始目录：")

target = input("请输入需要查找的目标文件：")
search_file(start_dir, target)

import os  # 导入os模块


all_files = os.listdir(os.curdir)  # 使用os.curdir表示当前目录更标准
type_dict = dict()

for each_file in all_files:
    if os.path.isdir(each_file):
        print(os.path.isdir(each_file))
        type_dict.setdefault("文件夹", 0)
        type_dict["文件夹"] += 1
    else:
        ext = os.path.splitext(each_file)[1]  # 分离文件名与扩展名，返回元组

        type_dict.setdefault(ext, 0)
        type_dict[ext] += 1


for each_type in type_dict.keys():
    print("该文件夹下共有类型为【{0}】的文件{1}个".format(each_type, type_dict[each_type]))

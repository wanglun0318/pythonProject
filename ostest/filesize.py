import os

all_files = os.listdir(os.curdir)  # 当前目录
file_dict = dict()

for each_file in all_files:
    if os.path.isfile(each_file):
        file_size = os.path.getsize(each_file)
        file_dict[each_file] = file_size

print(file_dict.items())
for each in file_dict.items():
    print("{0}【{1}Bytes】".format(each[0], each[1]))

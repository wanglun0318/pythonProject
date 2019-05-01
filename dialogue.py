
def save_file(boy, girl, count):
    file_name_girl = "girl_" + str(count) + ".txt"
    file_name_boy = "boy_" + str(count) + ".txt"

    boy_file = open(file_name_boy, "w")
    girl_file = open(file_name_girl, "w")

    boy_file.writelines(boy)
    girl_file.writelines(girl)

    boy_file.close()
    girl_file.close()


f = open("dialogue.txt")

boy = []
girl = []
count = 1


for each_line in f:
    if each_line[:6] != "======":
        # print(each_line.strip())
        each_line_str = each_line.strip()
        # print(each_line.split(":", 1))
        # print(each_line_str.split(":", 1))
        (role, line_spoken) = each_line.split(":", 1)  # 字符串切片
        if role == "客服":
            girl.append(line_spoken)
        elif role == "我":
            boy.append(line_spoken)
    else:
        print(boy)
        save_file(boy, girl, count)
        boy = []
        girl = []
        count += 1

save_file(boy, girl, count)

f.close()

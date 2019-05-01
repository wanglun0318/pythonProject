# file_new = input("请输入要打开的文件")
file_open = open(input("请输入要打开的文件"))

read_line = input("请输入需要显示的行数【格式如 13:20】:")

if read_line.strip() == ":":
    role = 1
    line_spoken = -1

(role, line_spoken) = read_line.split(":", 1)


count = 1


if role == "":
    role = 1

if line_spoken == "":
    line_spoken = -1

role = int(role)-1
line_spoken = int(line_spoken)
lines = line_spoken - role

for i in range(role):
    file_open.readline()

if lines < 0:
    print(file_open.read())
else:
    for j in range(lines):
        print(file_open.readline())

file_open.close()

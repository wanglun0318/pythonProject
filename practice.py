class Nstr(int):
    def __new__(cls, arg=0):
        if isinstance(arg, str):
            total = 0
            for each in arg:
                total += ord(each)
            arg = total
        print("11111")
        return int.__new__(cls, arg)


a = Nstr("qwert")
b = Nstr("asdfg")
print(a+b)

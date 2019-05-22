class Stack:
    def __init__(self):
        self.stack = []
       # for x in start:
        #    self.push(x)

    def isEmpty(self):
        return not self.stack

    def push(self, obj):
        self.stack.append(obj)

    def pop(self):
        if not self.stack:
            print("警告：栈为空！")
        else:
            return self.stack.pop()

    def top(self):
        if not self.stack:
            print("警告：栈为空！")
        else:
            return self.stack[0]

    def bottom(self):
        return self.stack


a = Stack()
a.push(1)
a.push(2)
a.push(3)
a.push(4)
a.push(5)
print(a.top())
print(a.pop())
print(a.isEmpty())
print(a.bottom())

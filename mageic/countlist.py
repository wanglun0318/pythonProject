"""
要求1： 实现获取，设置和删除一个元素的行为（删除一个元素的时候对应的计数器也会被删除）。
要求2：增加counter(index)方法,返回index参数所指定的元素记录的访问次数
要求3：实现append(), pop(), remove(), insert(), clear()和reverse(）方法（重写这些方法的时候注意
考虑计数器的对应改变）
"""


class CountList(list):
    def __init__(self, *args):  # 构造器，当一个实例被创建的时候调用的初始化方法
        super().__init__(args)
        self.count = []
        for i in args:
            self.count.append(0)

    def __len__(self):  # 当len()被调用时的行为（返回容器中元素的个数）
        return len(self.count)

    def __getitem__(self, key):
        # 定义获取容器中指定元素的行为，相当于self[key]
        self.count[key] += 1
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        # 定义设置容器中指定元素的行为，相当于self[key] = value
        self.count[key] += 1
        super().__setitem__(key, value)

    def __delitem__(self, key):
        # 定义删除容器中指定元素的行为，相当于del self[key]
        super().__delitem__(key)

    def counter(self, key):  # 用于查询指定元素的计数
        return self.count[key]

    def append(self, value):  # 用于在列表末尾添加新的对象
        self.count.append(0)
        super().append(value)

    def pop(self, key=-1):  # 用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
        del self.count[key]
        return super().pop(key)

    def remove(self, value):  # 用于移除列表中某个值的第一个匹配项。
        key = super().index(value)
        del self.count[key]
        super().remove(value)

    def insert(self, key, value):  # 用于将指定对象插入列表的指定位置
        self.count.insert(key, 0)
        super().insert(key, value)

    def clear(self):  # 方法用于移除集合中的所有元素
        self.count.clear()
        super().clear()

    def reverse(self):  # 用于反向列表中元素
        self.count.reverse()
        super().reverse()


c1 = CountList(1, 2, 3)
c1.reverse()
print(c1[0])
print(c1.counter(0))
print(c1.count)

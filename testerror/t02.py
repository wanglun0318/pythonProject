# 自己定义异常
# 自定义异常必须是系统异常的子类
class DanaValueError(ValueError):
    pass

try:
    print("111111111")
    # 手动引发一个异常
    # 语法： raise ErrorClassName
    raise DanaValueError
except NameError as e:
    print("NameError")
except ValueError as e:
    print("ValueError")
except Exception as e:
    print("有异常")
else:
    print("没有异常")
finally:
    print("我反正要执行！")
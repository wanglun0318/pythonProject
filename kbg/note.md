# 1.模块
- 一个模块就是一个包含python代码的文件，后缀名称是.py就可以。
- 模块就是python文件
- 为什么我们用模块
    - 程序太大，编写维护非常不方便，需要拆分
    - 模块可以增加代码重复利用的方式
    - 当作命名空间使用，避免命名冲突
    
- 如何定义模块
    - 模块就是一个普通文件，所以任何代码可以直接书写
    - 不过根据模块的规范，最好在模块中编写一下内容
        - 函数（单一功能）
        - 类（相似功能的组合，或者类似业务模块)
        - 测试代码
        
- 如何使用模块
    - 模块直接导入
        - 假如模块名称直接以数字开头，需要借助importlib帮助
        
    - 语法
        - import module_name (相对导入)
        - from.import p01 (绝对导入)
        - module_name.function_name
        - module_name.class_name
    - import模块as别名
        - 导入的同时给模块起一个别名
    - from module_name import func_name,class_name
        - 按上述方法有选择性的导入
        - 使用的时候可以直接使用导入的内容，不需要前缀
    - from module_name import *
        - 导入模块所有内容
- if __name__ == "__main__" 的使用
    - 可以有效避免模块代码被导入的时候被动执行的问题
    - 建议所有模块程序的入口都移除代码为入口
    
# 2.模块的搜索路径和存储
- 什么是模块的搜索路径：
    - 加载模块的时候，系统会在那些地方寻找此模块
- 系统默认的模块搜索路径
    - import sys
    - sys.path 属性可以获取路径列表、
- 添加搜索路径
    - sys.path.append(dir)
- 模块的加载顺序
    - 搜索内存中已经加载好的模块
    - 搜索python的内置模块
    - 搜索sys.path路径
    
#  包
- 包是一种组织管理代码的方式，包里面存放的是模块。
- 用于将模块包含在一起的文件夹就是包
- 自定义包的结构

    - |---包
    - |---|--- __init__.py  包的标志文件
    - |---|--- 模块1
    - |---|--- 模块2
    - |---|--- 子包(子文件夹)
    - |---|---|--- __init__.py  包的标志文件
    - |---|---|--- 子包模块1
    - |---|---|--- 子包模块2
    
-包的导入操作
    - import package_name
        - 直接导入一个包，可以使用_init_.py中的内容
        - 使用方式是：
            - package_name.func_name
            - package_name.class_name.func_name()
    - import package_name as p   
        - 导入的同时给包起一个别名
        - 注意的是此方法是默认对_inti_.py内容的导入
    - import package_module
        - 导入包中某一个具体的模块
        - 使用方法
            - package.module.func_name
            - package.module.class.fun()
            - package.module.class.var
    - import package.module as pm
    
- from ... import 导入
    - from package import module1,module2....
        - 此种方法导入不执行_inti_的内容
    - from package import *
        - 导入当前包_inti_.py文件中所有的函数和类
        - 使用方法
            - func_name()
            - class_name.func_name()
            - class_name.var
    - from package.module import *
        - 导入包中指定的模块的所有内容
        - 使用方法
            - func_name()
            - class_name.func_name()
            
- 在开发环境中经常会用其他模块，可以在当前包中直接导入其他模块中的内容
    - import 完整的包挥着模块路径
- _all_ 的用法
    - 在使用from package import * 的时候，*可以导入的内容
    - _inti_.py中如果文件为空，或者没有_all_,那么只可以把_inti_中的内容导入
    - _inti_.py中如果设置了_all_的值，那么则按照_all_指定的子包或者模块进行加载，如此则不会载入_inti_中内容
    - _all_=['module1','module2','package1'.......]
    
    
# 命名空间
- 用于区分不同位置不同功能但相同名称的函数挥着变量的一个特定前缀
- 作用是防止命名冲突
    - setName()
    - Student.setName()
    - Dog.setName()
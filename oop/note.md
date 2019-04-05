# 0.OOP-Python面向对象
-  Python的面向对象
-  面向对象编程
    -  基础
    -  公有私有
    -  继承
    -  组合，Mixin
-  魔法函数
    - 魔法函数概述
    - 构造类魔法函数
    - 运算类魔法函数
    
    
#  1.面向对象概述（ObjectOriented,  OO)
-  OOP思想
    - 接触到任意一个任务，首相 想到的是任务这个世界的构成是由模型构成的
-  名词
    - OO:面向对象
    - OOA:面向对象的分析
    - OOD:面向对象的设计
    - OOI:XXX的实现
    - OOP:XXX的编程
    - OOA->OOP->OOI: 面向对象的实现过程
    
    
# 2.类的基本实现
- 类的命名
    - 遵守变量命名的规范
    - 大驼峰（由一个或者多个单词构成，每个单词首字母大写，单词跟单词直接连接）
    - 尽量避开跟系统命名相似的命名
- 你如何声明一个类
    - 必须用Class关键字
    - 类由属性和方法构成，其他不允许出现
    - 成员属性定义可以直接使用变量赋值，如果没有值，允许使用None
- 实例化类
    -    变量 = 类名()   实例化一个对象
- 访问对象成员
    - 使用点操作符
        - obj.成员属性名称
        - obj.成员方法
- 可以通过默认内置变量检查类和对象的所有成员
    - 对象所有的成员检查
        - obj.__dict__    dict前后各有两个下划线


# 3. anaconda基本使用
- anaconda主要是一个虚拟环境管理器
- 还是一个安装包管理器
- conda list:  显示anaconda安装的包
- conda env list: 显示anaconda的虚拟环境列表
- conda create -n XXX python=3.6: 创建python版本为3.6的虚拟环境，名称为XXX
- conda activate XXX:  在window环境下激活运行虚拟环境
- conda deactivate:  在window环境下禁用虚拟环境
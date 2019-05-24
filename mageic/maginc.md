# 魔法方法
## 属性访问
    - __getattr__(self, name)
        - 定义当用户试图获取一个不存在的属性时的行为
        
    - __getattribute__（self, name)
        - 定义当该类的属性被访问时的行为
    
    - __setattr__(self, name, value)
        - 定义当一个属性被设置时的行为
    
    - __delattr__（self, name)
        - 定义当一个属性被删除时的行为
        
    - super()函数是用于调用父类的一个方法
        - 是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没问题，
        - 但是如果使用多继承，会涉及到查找顺序（MRO）,重复调用等种种问题
        - MRO就是类的方法解析顺序表，其实也就是继承父类方法是的顺序表
            - super()方法的语法：
            - super（type[, object-or-type]）
        
## 描述符
    - 描述符就是将某种特殊属性的类的实例指派给另一个类的属性
    
    - __get__(self, instance, owner)
        - 用于访问属性，它返回属性的值
        
    - __set__(self, instance, value)
        - 将在属性分配操作中调用，不返回任何内容
        
    - __delete__(self, instence)
        - 控制删除操作，不返回任何内容
    
## pickle模块
- python的pickle模块实现了基本的数据序列和反序列化。
- 通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久保存
- 通过pickle模块的反序列化操作，我们能偶从文件中创建上一次程序保存的对象。
- 基本接口：
    - pickle.dump(obj, file, [,protocol])
    - 有了pickle对象，就能对file以读取的形式打开
    - x = pickle.load(file)
    - 注解：从file中读取一个字符串，并将它重构为原来的python对象。
    - file：类文件对象，有read()和readline()接口
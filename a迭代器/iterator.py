'''
迭代器是指遵循迭代协议的对象
循环遍历的过程就是迭代
可迭代对象:可被for循环遍历的对象
可迭代对象实现需要__iter__   (返会可迭代对象本身) 或者__getitem__方法
__next__返回容器下一个元素无后续元素抛出Stoplteration异常
迭代器是一个可以记住遍历位置的对象,只能往前不能后退(会将所有数据加在内存里)

l=[1,2,3,4]
l.__iter__
#>>> l=[1,2,3,4]
#>>> l.__iter__
<method-wrapper '__iter__' of list object at 0x000002354B6B66C0>
#>>> from collections.abc import Iterable
#>>> isinstance(list(),Iterable)#列表和字典都是可迭代对象
True
isinstance判量的类型

生成器(generator):一类特殊的迭代器(不会将所有数据加在内存里)
生成器每次在迭代时可以返回一个或多个值,记录当前状态
创建方式:
1用yield关键字
def fib(n)
    current =0
    num1, num2 =0, 1
    while current < n:
        num= num1
        num1. num2 =num2, num1+num2
        current +=1
        yield num
    return done
g=fib(5)
type(g)

输出:generator

生成器取值
next和send:next去取下一个元素
           send取下一个值,同时可以向生成器中传递一个值
           next等同于send(none),第一次取值需要用next或send(None)
2用生成器表达式(推导式)   G=(x*2 for x in range(5))


'''


def fib(n):  # 斐波那契额数列
    current = 0
    num1, num2 = 0, 1
    while current < n:
        num = num1
        num1, num2 = num2, num1 + num2
        current += 1
        yield num  # yield执行过程 当程序执行到yield处时,生成器暂停返回当前值,等待下一次唤醒(next,sed)
    return 'done'


g = fib(5)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(g.send(None))

"""
装饰器
@装饰器名
def fun():
    pass 
    
    功能:本质是一个函数,可以再不改变代码结构的情况下给代码添加新功能,装饰器工作过程
    将被当装饰的函数当做参数传递给装饰器函数(名称相同的函数),并返回装饰后被装饰的函数
    是闭包的一种应用
    
    它经常用于有切面需求的场景，比如：插入日志、性能测试、事务处理、缓存、权限校验等场景，
    装饰器是解决这类问题的绝佳设计。有了装饰器，我们就可以抽离出大量与函数功能本身无关的雷
    同代码到装饰器中并继续重用。概括的讲，装饰器的作用就是为已经存在的对象添加额外的功能。
    
    缺点:会丢失部分信息如名字,文档注释注解等
闭包:函数机器相关引用环境组合成的实体
闭包中不可以直接修改外部函数的局部变量
--类似不能在函数中修改全局变量,需要关键字nonlocal
---闭包作用: 闭包执行完后仍能保持当前内部环境
           闭包可根据外部作用域变量来得到不同的结果 
    https://www.runoob.com/w3cnote/python-func-decorators.html
    
wraps:为保留因装饰器丢失信息而提供的装饰器  
       
"""

from functools import wraps
def light(func):
    print("获得神光棒x1")
    #这是注释

    '''加了wraps
    Help on function person in module __main__:

person()
    呵呵哈哈哈或或

不加
    Help on function tiga in module __main__:
    
    tiga()
    #@wraps(func)

    '''

    @wraps(func)
    def tiga(*args, **kwargs):  # cls为类,args是一个数组，kwargs一个字典
        func()
        print("可~,n我是光之巨人\n")

    return tiga


def light1(func):
    print("获得神光棒x1")

    def tiga():
        func()
        print("可~,n我是光之巨人\n")

    return tiga


@light
def person():
    """呵呵哈哈哈或或"""
    print("我是某胜利队队员大骨")


def person1():
    #呵呵哈哈哈或或
    print("我是某胜利队队员大骨tang")


person()#用装饰器
dagu=person.__wrapped__#解除装饰器
dagu()
print("\n")
light1(person1)()#以函数person1为参数
help(person)
'''获得神光棒x1
我是某胜利队队员大骨
可~,n我是光之巨人'''
'''
带参数的装饰器
装饰器还有更大的灵活性，例如带参数的装饰器，在上面的装饰器调用中，该装饰器接收
唯一的参数就是执行业务的函数 foo 。装饰器的语法允许我们在调用时，提供其它参数，
比如@decorator(a)。这样，就为装饰器的编写和使用提供了更大的灵活性。比如，我们
可以在装饰器中指定日志的等级，因为不同业务函数可能需要的日志级别是不一样的。
def use_logging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "warn":
                logging.warn("%s is running" % func.__name__)
            elif level == "info":
                logging.info("%s is running" % func.__name__)
            return func(*args)
        return wrapper

    return decorator

@use_logging(level="warn")
def foo(name='foo'):
    print("i am %s" % name)

foo()
上面的 use_logging 是允许带参数的装饰器。它实际上是对原有装饰器的一个函数封装，
并返回一个装饰器。我们可以将它理解为一个含有参数的闭包。当我 们使用
@use_logging(level="warn")调用的时候，Python 能够发现这一层的封装，并把参
数传递到装饰器的环境中。

@use_logging(level="warn") 等价于 @decorator
'''
'''装饰器也还可以是类
__call__:魔法方法可以让类像方法一样调用

'''

"""
实验
1,用for对数据做迭代


"""





































































from time import sleep


# 面向对象  描述一个时钟
def main():
    time = Clock(00, 00, 00)
    while 1:
        time.run()
        time.show()
        sleep(1)


class Clock:
    # 数字时钟
    def __init__(self, mnt, tm, second):
        '''
        第一个参数是实例对象本身，并且约定俗成，把其名字写为self。其作
        用相当于java中的this，表示当前类的对象，可以调用当前类中的属性
        和方法,self必须在第一个参数，__init__特殊方法用来构造方法
        '''
        self.tm = tm  # 时
        self.mnt = mnt  # 分
        self.second = second  # 秒

    '''
    如果希望属性是私有的，在给属性命名时可以用两个下划线作为开头
    因为在很多面向对象编程语言中，我们通常会将对象的属性设置为私有
    的（private）或受保护的（protected），简单的说就是不允许外界
    访问，而对象的方法通常都是公开的（public）   
    '''

    def run(self):  # 运行
        self.second += 1
        if self.second == 60:
            self.mnt += 1
            self.second = 0
            if self.mnt == 60:
                self.tm += 1
                self.mnt = 0
                if self.tm == 24:
                    self.tm = 0

    def show(self):
        print(f"{self.tm}:{self.mnt}:{self.second}")


main()

class Dog():
    # 模拟小狗类
    def __init__(self, name):
        self.name = name

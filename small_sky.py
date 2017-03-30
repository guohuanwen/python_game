# coding=utf-8
import re

#循环语句，if语句，正则表达式
def day1():
    text = '111h222e333l444l5o34w47o88r9066l456d'
    for i in text:
        pattern = re.compile(r'\d')
        match = pattern.match(i)
        if not match:
            print(i)

#条件语句，函数，递归，数值运算
def day2(num):
    if num > 0:
        return day2(num -1)
    elif num < 0:
        return day2(num + 1)
    else:
        return num

# print(day2(day2(-12)))

class People:
    def __init__(self):
        print('SmallSkyFather init')

    def sleep(self):
        print('SmallSkyFather sleep')

class SmallSky(People):
    def __init__(self):
        People.__init__(self)

    def sleep(self):
        print('SmallSky need turn off the lights ')
        People.sleep(self)

#面向对象1
#继承父类方法，代码逻辑按层次封装，简化问题
#抽象出事物共同属性，行为，子类共用这部分代码，子类扩展父类属性，行为
def day3():
    small_sky = SmallSky()
    small_sky.sleep()

# day3()


#面向对象2
#类似于厨师不关心菜怎么来，有人负责种菜，有人负责做菜，单一职责
#整个社会也在这样一种体系下运行，更符合人的思维习惯
#省略几万字。。。

#移位运算，移位运算计算速度优于除法，16／4 优化-————> 16>>2
def day4():
    print(201>>2)#右移（低位丢弃） 200的二进制数11001001 右移后 110010 ，110010转十进制50
    print(2<<2)#左移（高位丢弃，低位补0） 2的二进制数10， 10左移后1000， 1000转十进制8

day4()
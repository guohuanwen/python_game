# coding:utf-8

import re
from PIL import Image
import os, sys
import matplotlib


# 循环语句，if语句，正则表达式
def day1():
    text = '111h222e333l444l5o34w47o88r9066l456d'
    for i in text:
        pattern = re.compile(r'\d')
        match = pattern.match(i)
        if not match:
            print(i)


# 条件语句，函数，递归，数值运算
def day2(num):
    if num > 0:
        return day2(num - 1)
    elif num < 0:
        return day2(num + 1)
    else:
        return num


# print(day2(day2(-12)))

class People:
    def __init__(self):
        print('People init')

    def sleep(self):
        print('People sleep')


class SmallSky(People):
    def __init__(self):
        People.__init__(self)

    def sleep(self):
        print('SmallSky need turn off the lights ')
        People.sleep(self)


class Bigwen(People):
    def __init__(self):
        People.__init__(self)

    def eat(self):
        print('Bigwen eats food')


class OtherPeople(SmallSky, Bigwen):
    def __init__(self):
        SmallSky.__init__(self)

    def drink(self):
        print('OtherPeople drinks water')


# 面向对象1
# 继承父类方法，代码逻辑按层次封装，简化问题
# 抽象出事物共同属性，行为，子类共用这部分代码，子类扩展父类属性，行为
def day3():
    other = OtherPeople()
    other.sleep()
    other.eat()
    other.drink()


# day3()


# 面向对象2
# 类似于厨师不关心菜怎么来，有人负责种菜，有人负责做菜，单一职责
# 整个社会也在这样一种体系下运行，更符合人的思维习惯
# 省略几万字。。。

# 移位运算，移位运算计算速度优于除法，16／4 优化-————> 16>>2
def day4():
    print(201 >> 2)  # 右移（低位丢弃） 201的二进制数11001001 右移后 110010 ，110010转十进制50
    print(2 << 2)  # 左移（高位丢弃，低位补0） 2的二进制数10， 10左移后1000， 1000转十进制8


# day4()

def day5():
    print('1，熟悉window下环境变量的配置')
    print('2，pip使用')
    print('3，cmd的使用')
    print('windows Python和pip安装  http://www.cnblogs.com/yuanzm/p/4089856.html')


class TranslateImg:
    def __init__(self):
        self.imagepath = 'img.jpeg'
        self.filepath = 'img.txt'

    def translate(self):
        ww = 100
        img = Image.open(self.imagepath)
        # 转黑白
        img = img.convert('L')
        width, height = img.size
        rate = width / ww
        width = int(ww)
        height = int(height / rate)
        img = img.resize((width, height))
        pix = img.load()
        text = open(self.filepath, "w")
        aa = ""
        for h in range(0, height, 1):
            for w in range(0, width, 1):
                st = self.string_replace(pix[w, h])
                text.write(st)
                aa = aa + st
                if w == ww - 1:
                    text.write("\n")
        text.close

    def string_replace(self, number):
        replace_text = 'smallsky_is_a_girl'
        param = 20
        n = int(number / param)
        j = int(255 / param)
        for i in range(0, j, 1):
            if (n == i):
                return replace_text[n]
        return "."

def day6():
    print('图形库PIL的简单应用：图片转字符串画')
    print('1，运行代码。2，用文档打开当前目录下的img.txt（网页打开：https://github.com/guohuanwen/python_game/blob/master/img.txt。原图打开：https://github.com/guohuanwen/python_game/blob/master/img.jpeg）')
    translateImg = TranslateImg()
    translateImg.translate()

def day7():
    text = open("over.txt","r")
    for i in text.readlines():
        print(str(i))

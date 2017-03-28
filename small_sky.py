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

print(day2(day2(-12)))
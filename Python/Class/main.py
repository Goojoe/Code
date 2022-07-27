#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Class 
@File    ：main.py
@Author  ：咕咕乔
@Date    ：2022/5/31 12:31 
@About   : 
'''
class People(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.jump()

    def walk(self):
        print('我的名字叫作：{}，我正在走路'.format(self.name))

    def eat(self):
        print('我的名字叫作：{}，我正在吃饭'.format(self.name))

    def jump(self):
        print('我的名字叫作：{}，我跳了一下'.format(self.name))


xiaoer = People('王小二', 18)
zhangsan = People('张三', 30)
print('=============获取对象的属性=============')
print(xiaoer.name)
print(zhangsan.age)

print('=============执行对象的方法==============')
xiaoer.walk()
zhangsan.eat()

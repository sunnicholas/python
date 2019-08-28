# -*- coding: utf-8 -*

# method
# Python 中有一个类似的概念，叫方法（method）。方法是与指
# 定数据类型紧密相关的函数。方法与函数一样，可执行代码并返回结果。不同的是，只
# 有在对象上才能调用方法。同样也可以传递参数给方法。

print "Hello".upper()

print "Hello".replace("o","@")



# list
# 列表（list）是以固定顺序保存对象的容器

friut = list()
print friut

friut = []
print friut

friut = ["Apple","Orange","Pear"]
print friut

friut.append("Banana")
friut.append("Peach")
print friut

random = []
random.append(True)
random.append(100)
random.append(1.1)
random.append('Hello')
print random

# 字符串、列表和元组都是可迭代的（iterable）。如果可以使用循环访问对象中的每一
# 个元素，那么该对象是可迭代的，被称为可迭代对象。可迭代对象中的每一个元素都有
# 一个索引（index），即表示元素在可迭代对象中位置的数字。列表中第一个元素的索引
# 是 0，而不是 1。

print friut[0]
print friut[1]
print friut[2]

# 列表是可变的（mutable）。如果一个容器是可变的，则可以向该容器中增删对象。
# 将列表中某个元素的索引赋给一个新的对象，即可改变该元素

colors = ["blue","green","yellow"]
print colors
item = colors.pop()
print item
print colors

print friut+colors

print "green" in colors
print "black" not in colors
# print (unicode("使用函数 len 可获得列表的大小", encoding="utf-8")).join(len(colors))

print '使用函数 len 可获得列表的大小',len(colors)



def colorsfun():
    """
    []他是列表
    ()元组
    {}字典==php的数组
    """
    colors = ["purple",
              "orange",
              "yellow",
              "red",
              "black"]
    try:
        guess = input("Guess a color:")

        if guess in colors:
            print "You guessed correctly!!"
        else:
            print ("Wrong ! Try again")
    except (NameError,SyntaxError):
        print ("use the format as 'xxxx'or \"xxx\"")
        colorsfun()
colorsfun()


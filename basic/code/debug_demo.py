"""
这个代码主要是实现if,for,while以及鸡蛋问题
作者：岳润雨
日期：2017-9-20
"""


def if_demo():
    print("if的例子")
    a = True
    if a:
        print("哈哈，我是真的。")
    else:
        print("哼哼，我是假的。")


def for_demo():
    print("for的例子")
    str1 = "beautiful"
    for i in str1:
        print(i)


def while_demo():
    print("while的例子")
    i = 5
    while i > 0:
        print(i)
        i -= 1

def egg():
    for i in range(1000):
        if i%4!=1:
            continue
        if i%5!=4:
            continue
        if i%6!=3:
            continue
        if i%7!=5:
            continue
        if i%8!=1:
            continue
        if i%9!=0:
            continue
        print(i)
if __name__ == "__main__":
    if_demo()
    for_demo()
    while_demo()
    egg()

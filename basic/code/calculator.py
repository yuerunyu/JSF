"""
这是一个计算器的演示程序；
作者：岳润雨
日期：2017-9-19
"""


def add(a, b):
    """
    加法运算
    :param a:
    :param b:
    :return:
    """
    return a + b


def subtract(a, b):
    """
    减法运算
    :param a:
    :param b:
    :return:
    """
    return a - b


def multipy(a, b):
    """
    乘法运算
    :param a:
    :param b:
    :return:
    """
    return a * b


def divide(a, b):
    """
    除法运算
    :param a:
    :param b:
    :return:
    """
    assert b != 0
    return a / b


if __name__ == "__main__":
    jia = add(1, 2)
    jian = subtract(3, 4)
    cheng = multipy(5, 6)
    chu = divide(7, 8)
    print(jia, jian, cheng, chu)
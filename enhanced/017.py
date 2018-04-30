def hello():
    print('hello!')
    return
    print("i love you")


def power(x, y):
    return (x ** y)


# print(power(2, 3))


def gcd(x, y):
    """
    这个函数是欧几里得函数，也就是求两个数的最大公约数；
    :param x:
    :param y:
    :return:
    """
    while y:
        x, y = y, x % y
    return x


def Dec2Bin(dec):
    """
    这个函数实现了十进制转换为二进制；
    :param dec:
    :return:
    """
    temp = []
    result = ''

    while dec:
        quo = dec % 2
        dec = dec // 2
        temp.append(quo)
    while temp:
        result += str(temp.pop())
    return result
print(Dec2Bin(25))
"""
这节课学习的内容：
1、使用def加函数名称的方式来定义一个函数，函数名称后边要跟一个小括号；
2、调用函数的时候，直接输入函数的名字即可；
3、函数要有返回值，一旦遇到返回值，就不会继续往下执行了。
"""

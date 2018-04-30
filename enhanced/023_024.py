"""
023_024课程内容：
1、讲解了汉诺塔实现的原理，主要就是将问题细化；
2、兔子生育问题，先把对应的数学表达式罗列出来，使用函数实现。
3、并不是所有问题用递归解决都很好，因为递归是函数本身的调用，非常耗内存，并且返回条件如果设置不正确，很容易出错。
"""
def hanoi(n, x, y, z):
    if n == 1:
        print(x, "--->", z)
    else:
        hanoi(n - 1, x, z, y)
        print(x, "--->", z)
        hanoi(n - 1, y, x, z)


def func1(n):
    result = ''
    if n:
        result = func1(n // 2)
        return result + str(n % 2)
    else:
        return result


def func2(n):
    if n:
        list1.insert(0, n % 10)
        func2(n // 10)
        return list1


list1 = []
print(func2(12345))


# def old_test(n):
#     if n == 1:
#         return 10
#     else:
#         return 2 + old_test(n - 1)
#
#
# n = int(input('请输入几个人：'))
#
# print("哈哈，我知道第%d个人是%d岁啦！！" % (n, old_test(n)))



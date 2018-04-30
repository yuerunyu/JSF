def CharTrans1(string):
    """
    字符串转换函数，可以将驼峰式转换为下划线式
    :param string:
    :return:
    """
    b = []
    for i in range(len(string)):
        if string[i].isupper():
            b.append('_')
            # print(b)
        b.append(string[i].casefold())
    c = "".join(b)
    print(c)


def CharTrans2(string):
    """
    字符串转换函数，可以将下划线式转换为驼峰式
    :param string:
    :return:
    """
    a = string.split("_")
    # print(a)
    c = "".join(i.title() for i in a)
    print(c)


if __name__ == "__main__":
    CharTrans1('iLoveFishC')
    CharTrans2('i_love_fishc')

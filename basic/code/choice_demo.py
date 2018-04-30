def add():
    """
    这是一个加法函数
    :param a:
    :param b:
    :return:
    """
    a = int(input("please input your num1:"))
    b = int(input("please input your num2:"))
    c = a + b
    print("加法运算得到的结果是：%d" % (c))


def subtract():
    """
    这是一个减法函数,subtract
    :param a:
    :param b:
    :return:
    """
    a = int(input("please input your num1:"))
    b = int(input("please input your num2:"))
    c = a - b
    print("减法运算得到的结果是：%d" % (c))


def multipy():
    """
    这是一个乘法函数
    :param a:
    :param b:
    :return:
    """
    a = int(input("please input your num1:"))
    b = int(input("please input your num2:"))
    c = a * b
    print("乘法运算得到的结果是：%d" % (c))


def divide():
    """
    这是一个除法函数
    :param a:
    :param b:
    :return:
    """

    a = int(input("please input your num1:"))
    b = int(input("please input your num2:"))
    assert b != 0
    c = a / b
    print("除法运算得到的结果是：%d" % (c))


def showmenu():
    """
    菜单函数
    主要是给予用户选择。
    :return:
    """
    prompt = '''
|--- 加法运算：A/a ---|
|--- 减法运算：S/s ---|
|--- 乘法运算：M/m ---|
|--- 除法运算：D/d ---|
|--- 退出程序：Q/q ---|
|--- 请输入指令代码：'''

    while True:
        chosen = False
        while not chosen:
            choice = input(prompt)
            if choice not in 'AaSsMmDdQq':
                print('您输入的指令代码错误，请重新输入!')
            else:
                chosen = True

        if choice == 'Q' or choice == 'q':
            break
        if choice == 'A' or choice == 'a':
            add()
        if choice == 'S' or choice == 's':
            subtract()
        if choice == 'M' or choice == 'm':
            multipy()
        if choice == 'D' or choice == 'd':
            divide()


if __name__ == "__main__":
    showmenu()

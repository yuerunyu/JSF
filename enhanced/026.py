"""
026课程内容：
1、fromkeys方法
2、keys values items
3、get方法
4、clear方法
5、copy方法，浅拷贝
6、setdefault方法
7、update方法
8、字典不可以一键多值，因为对同一个键赋值两次，最后的赋值会将前边的赋值覆盖掉；
9、字典的键要求比较高，必须是可哈希的，如一些可变类型（变量，列表，字典本身等）都不可以作为字典的键。
"""
db = {}


def new():
    name = input('请输入用户名：')
    if name not in db:
        passwd = input("请输入密码：")
        db[name] = passwd  # 这里不用fromkeys方法是因为该方法是创建并返回一个字典，我们在前面已经创建好字典了。
        print("注册成功，赶紧试试登陆吧！")



    else:
        print("此用户名已经被使用，")
        name = input("请重新输入：")
        passwd = input("请输入密码：")
        db[name] = passwd
        print("注册成功，赶紧试试登陆吧！")


def login():
    name = input('请输入用户名：')
    while True:
        if name in db:
            passwd = input("请输入密码：")
            if passwd == db[name]:
                print("欢迎进入XXOO系统，请点击右上角的X结束程序！")
                name = input('请输入用户名：')
            else:
                return -1
        if name not in db:
            name = input("您输入的用户名不存在，请重新输入：")


def menu():
    prompt = '''|---欢迎进入通讯录程序---|
|---新建用户：N/n---|
|---登陆账号：L/l---|
|---退出程序：Q/q---|
|---请输入指令代码：'''

    while True:
        code = input(prompt)
        if code == "N" or code == "n":
            new()
        if code == "L" or code == "l":
            login()
        if code == "Q" or code == "q":
            break
menu()

#这个例子比较好的地方就是做了更加全面的考虑，加入了很多标志位，可以控制住用户的输入。
# user_data = {}
#
#
# def new_user():
#     prompt = '请输入用户名：'
#     while True:
#         name = input(prompt)
#         if name in user_data:
#             prompt = '此用户名已经被使用，请重新输入：'
#             continue
#         else:
#             break
#
#     passwd = input('请输入密码：')
#     user_data[name] = passwd
#     print('注册成功，赶紧试试登录吧^_^')
#
#
# def old_user():
#     prompt = '请输入用户名：'
#     while True:
#         name = input(prompt)
#         if name not in user_data:
#             prompt = '您输入的用户名不存在，请重新输入：'
#             continue
#         else:
#             break
#
#     passwd = input('请输入密码：')
#     pwd = user_data.get(name)
#     if passwd == pwd:
#         print('欢迎进入XXOO系统，请点右上角的X结束程序！')
#     else:
#         print('密码错误！')
#
#
# def showmenu():
#     prompt = '''
# |--- 新建用户：N/n ---|
# |--- 登录账号：E/e ---|
# |--- 推出程序：Q/q ---|
# |--- 请输入指令代码：'''
#
#     while True:
#         chosen = False
#         while not chosen:
#             choice = input(prompt)
#             if choice not in 'NnEeQq':
#                 print('您输入的指令代码错误，请重新输入：')
#             else:
#                 chosen = True
#
#         if choice == 'q' or choice == 'Q':
#             break
#         if choice == 'n' or choice == 'N':
#             new_user()
#         if choice == 'e' or choice == 'E':
#             old_user()
#
#
# showmenu()




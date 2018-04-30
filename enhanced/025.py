"""
025课程内容：
1、字典不是序列类型，是映射类型；
2、字典是由键和值组成的；
3、创建一个字典可以有很多种方法，使用dict函数的时候要注意，这个函数只能有一个参数，但是这个参数可以是元组，可以是列表。
"""
print('|---欢迎进入通讯录程序---|')
print('|---1、查询联系人资料 ---|')
print('|---2、插入新的联系人 ---|')
print('|---3、删除已有联系人 ---|')
print('|---4、退出通讯录程序 ---|')
db = {}#创建一个新的字典，用来存储数据！
code = int(input("请输入相关的指令代码："))
while code != 4:
    if code == 1:
        name = input('请输入联系人姓名：')
        if name not in db:
            print("此用户不存在！")
            code = int(input("请输入相关的指令代码："))
        if name in db:
            print(name + ':' + db[name])
            code = int(input("请输入相关的指令代码："))

    if code == 2:
        name = input('请输入联系人姓名：')
        if name in db:
            print("您输入的姓名在通讯录中已经存在-->>", name + ':' + db[name])
            change = input("是否修改用户资料（YES/NO）：")
            if change == "YES":
                number = input('请输入用户联系电话：')
                db[name] = number
            if change == "NO":
                code = int(input("请输入相关的指令代码："))
                continue
            code = int(input("请输入相关的指令代码："))
        if name not in db:
            number = input('请输入用户联系电话：')
            db[name] = number
            code = int(input("请输入相关的指令代码："))
    if code == 3:
        name = input('请输入联系人姓名：')
        if name in db:
            del (db[name])
            print('删除成功！')
        else:
            print('您输入的姓名不在联系人当中！')

if code == 4:
    print('|---感谢使用通讯录程序 ---|')







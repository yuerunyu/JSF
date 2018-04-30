"""
030课程内容：
1、OS模块
2、os.path模块
"""
#统计当前目录下每个文件类型的文件数
# import os
# os.chdir('E:\常用软件')
# a = b = c = d = e = 0
# list1 = os.listdir(os.curdir)  # 包含此目录下的所有文件名的一个列表
# for i in range(len(list1)):
#     # list2=list1[i].split('.')#打印出list2的内容就是['1-理赔申请书-空白表', 'pdf']
#     if list1[i][(len(list1[i]) - 3):] == 'rar':
#         a += 1
#     if list1[i][(len(list1[i]) - 3):] == 'exe':
#         b += 1
#     if list1[i][(len(list1[i]) - 3):] == 'doc':
#         c += 1
#     if list1[i][(len(list1[i]) - 3):] == 'zip':
#         d += 1
#     if list1[i][(len(list1[i]) - 3):] == 'txt':
#         e += 1
# print('该文件夹下共有类型为【.rar】的文件%d个' % (a))
# print('该文件夹下共有类型为【.exe】的文件%d个' % (b))
# print('该文件夹下共有类型为【.doc】的文件%d个' % (c))
# print('该文件夹下共有类型为【.zip】的文件%d个' % (d))
# print('该文件夹下共有类型为【.txt】的文件%d个' % (e))
#以上的实现方法并不是最优的，因为会有很多我们并不知道的文件类型存在，这样的话就遍历不到那些文件了。

# import os
#
# os.chdir('E:\常用软件')
# all_list = os.listdir(os.curdir)
# type_dict = dict()
# for file in all_list:
#     if os.path.isdir(file):
#         type_dict.setdefault('文件夹', 0)  # 使用字典和字典的setdefault方法，setdefault()方法有两个参数，第一个参数就是要检查的键；
#         # 第二个参数则是如果该键不存在的时候要设置的值。如果该键确实存在，则默认值不会起作用，并返回键的值。
#         type_dict['文件夹'] += 1
#
#     else:
#         ext = os.path.splitext(file)[1]
#         type_dict.setdefault(ext, 0)
#         type_dict[ext] += 1
#
# for each_type in type_dict.keys():
#     print('该文件夹下共有类型为【%s】的文件 %d 个' % (each_type, type_dict[each_type]))





#计算目录下所有文件的大小
# import os
# os.chdir('E:\常用软件')
# all_list = os.listdir(os.curdir)
# for file in all_list:
#     if os.path.isfile(file):
#         print("%s : 【%d字节】" % (file,os.path.getsize(file)))



#输入路径和待查找的文件，返回查找结果
#之所以这样执行成功的原因是待查找的文件所在的目录或者上一层目录没有别的文件，最好的方法还是使用递归调用比较合适。
# import os
# folder=input('请输入待查找的初始目录：')
# file=input('请输入需要查找的目标文件：')
# tuple1=os.walk(folder)
# for i in tuple1:
#     print(i)
#     if i[2][0] == file:
#         print(i[0]+'\\'+i[2][0])




#在指定路径下搜索指定格式的文件，并将搜索到的文件路径存入一个新的文件中。
# import os
# import os.path
#
#
# def search_file(start_dir, target):
#     os.chdir(start_dir)
#
#     for each_file in os.listdir(os.curdir):
#         ext = os.path.splitext(each_file)[1]
#         if ext in target:
#             vedio_list.append(os.getcwd() + os.sep + each_file + os.linesep)
#             print(vedio_list)
#
#         if os.path.isdir(each_file):
#             search_file(each_file, target)  # 递归调用
#             os.chdir(os.pardir)  # 递归调用后切记返回上一层目录
#
#
# start_dir = input('请输入待查找的初始目录：')
#
# target = ['.exe', '.zip', '.rar']
# vedio_list = []
# search_file(start_dir, target)
# f = open('E:/vediolist.txt', 'w')
# f.writelines(vedio_list)
# f.close()




import os


def print_pos(key_dict):
    keys = key_dict.keys()
    keys = sorted(keys)  # 由于字典是无序的，我们这里对行数进行排序
    for each_key in keys:
        print('关键字出现在第 %s 行，第 %s 个位置。' % (each_key, str(key_dict[each_key])))


def pos_in_line(line, key):
    pos = []
    begin = line.find(key)
    while begin != -1:
        pos.append(begin + 1)  # 用户的角度是从1开始数
        begin = line.find(key, begin + 1)  # 从下一个位置继续查找

    return pos


def search_in_file(file_name, key):
    f = open(file_name)
    count = 0  # 记录行数
    key_dict = dict()  # 字典，用于存放key所在具体行数对应具体位置

    for each_line in f:
        count += 1
        if key in each_line:
            pos = pos_in_line(each_line, key)  # key在每行对应的位置
            key_dict[count] = pos

    f.close()
    return key_dict


def search_files(key, detail):
    all_files = os.walk(os.getcwd())
    txt_files = []

    for i in all_files:
        for each_file in i[2]:
            if os.path.splitext(each_file)[1] == '.txt':  # 根据后缀判断是否文本文件
                each_file = os.path.join(i[0], each_file)
                txt_files.append(each_file)

    for each_txt_file in txt_files:
        key_dict = search_in_file(each_txt_file, key)
        if key_dict:
            print('================================================================')
            print('在文件【%s】中找到关键字【%s】' % (each_txt_file, key))
            if detail in ['YES', 'Yes', 'yes']:
                print_pos(key_dict)


key = input('请将该脚本放于待查找的文件夹内，请输入关键字：')
detail = input('请问是否需要打印关键字【%s】在文件中的具体位置（YES/NO）：' % key)
search_files(key, detail)







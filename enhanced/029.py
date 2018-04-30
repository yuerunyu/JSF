"""
029课程内容：
文件系统OS模块
"""
#编写程序，接受用户的输入，并保存成文件。

# def file_write(file_name):
#     f = open(file_name, 'w')
#     print('请输入内容【单独输入\':w\'保存退出】：')
#
#     while True:
#         write_some = input()
#         if write_some != ':w':
#             f.write('%s\n' % write_some)
#         else:
#             break
#
#     f.close()
#
# file_name = input('请输入文件名：')
# file_write(file_name)

#编写程序，比较用户输入的两个文件，如果不同，显示出所有不同处的行号和第一个不同字符的位置

# def file_compare(file1, file2):
#     f1 = open(file1)
#     f2 = open(file2)
#     count = 0 # 统计行数
#     differ = [] # 统计不一样的数量
#
#     for line1 in f1:
#         line2 = f2.readline()
#         count += 1
#         if line1 != line2:
#             differ.append(count)
#
#     f1.close()
#     f2.close()
#     return differ
#
# file1 = input('请输入需要比较的头一个文件名：')
# file2 = input('请输入需要比较的另一个文件名：')
#
# differ = file_compare(file1, file2)
#
# if len(differ) == 0:
#     print('两个文件完全一样！')
# else:
#     print('两个文件共有【%d】处不同：' % len(differ))
#     for each in differ:
#         print('第 %d 行不一样' % each)

#编写程序，当用户输入文件名和行数后，将该文件的前N行内容打印在屏幕上。
# def file_view(filename,lines):
#     file=open(filename)
#     print('文件', filename, '的前%d行内容如下：' % lines)
#     while lines:
#         print(file.readline(), end = '')
#         lines -= 1
#     file.close()
# filename = input('请输入要打开的文件（E:\\test.txt）：')
# lines = int(input('请输入需要显示该文件前几行：'))
# file_view(filename,lines)

#在上一个的基础上，增加功能，比如客户输入指定的行数，1：3，这样打印的就是第一行到第三行，如果输入的是3：，说明需要打印第三行到结束；
# def file_view(file_name, line_num):
#     if line_num.strip() == ':':
#         begin = '1'
#         end = '-1'
#
#     (begin, end) = line_num.split(':')
#
#     if begin == '':
#         begin = '1'
#     if end == '':
#         end = '-1'
#
#     if begin == '1' and end == '-1':
#         prompt = '的全文'
#     elif begin == '1':
#         prompt = '从开始到%s' % end
#     elif end == '-1':
#         prompt = '从%s到结束' % begin
#     else:
#         prompt = '从第%s行到第%s行' % (begin, end)
#
#     print('\n文件%s%s的内容如下：\n' % (file_name, prompt))
#
#     begin = int(begin) - 1
#     end = int(end)
#     lines = end - begin
#
#     f = open(file_name)
#
#     for i in range(begin):  # 用于消耗掉begin之前的内容
#         f.readline()
#
#     if lines < 0:
#         print(f.read())
#     else:
#         for j in range(lines):
#             print(f.readline(), end = '')
#     f.close()
# file_name = input(r'请输入要打开的文件（C:\\test.txt）：')
# line_num = input('请输入需要显示的行数【格式如 13:21 或 :21 或 21: 或 : 】：')
# file_view(file_name, line_num)

#替换文章中的字符，实现全部替换的功能。

def file_replace(file_name,old,new):

    file=open(file_name)
    count=0
    string=str(file.readlines())
    for each in string:
            if each==old:
                        count+=1
    string1=string.replace(old,new)
    file.close()
    print('文件',file_name,'共有%d个【%s】' % (count,old))
    print('您确定要把所有的【%s】替换为【%s】吗？' % (old,new))
    Y_N=input('【YES/NO】：')
    if Y_N == 'yes':
        file=open(file_name,'w')
        file.writelines(string1)
        file.close()
    else:
        file.close()
file_name=input('请输入文件名：')
old=input('请输入需要替换的单词或字符：')
new=input('请输入新的单词或字符：')
file_replace(file_name,old,new)







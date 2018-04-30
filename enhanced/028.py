"""
028课程内容：
1、文件的操作，使用open函数打开一个文件。
2、文件对象方法
3、文件打开模式

"""
# f = open ('E:\OpenMe.mp3')
# for each_line in f:
#     print(each_line,end='')
# f.close()
f1=open('E:\OpenMe.mp3')
f2=open('E:\OpenMe.txt','x')
f2.write(f1.read())
f2.close()
f1.close()
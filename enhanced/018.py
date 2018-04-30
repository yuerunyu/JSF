"""
18课时学习的内容：
1、函数的参数：
    形参：函数创建和定义过程中小括号里的参数
    实参：函数在调用过程中传递的参数
    默认参数：在参数定义的过程中，为形参赋初值，当函数调用的时候，如果不传递实参，则使用默认参数
    关键字参数：在函数调用的过程中，通过参数名制定需要赋值的参数，这样做就不怕因为搞不清楚参数的顺序而导致函数调用出错
    收集参数：使用*，可以机动的定义参数，传入的是一个元组
"""
# def test(*para):
#     """
#     收集参数
#     :param args:
#     :return:
#     """
#     print("参数的长度是" , len(para))
#     print("第二个参数是" , para[1])
# # test(1,2,3,4)
#
# def Myfunc(*param,base=3):
#     """
#     计算打印所有参数的和乘以基数3的结果；
#     如果最后一个参数为5，则将基数修改为5，基数不参与求和；
#     :param param:
#     :param base:
#     :return:
#     """
#     result=0
#     for i in param:
#         result=i+result
#     result=result*base
#     print("结果是：",result)
# Myfunc(1,2,3,4,5,base=5)

# def Narcissus():
#     for each in range(100, 1000):
#         temp = each
#         sum = 0
#         while temp:
#             sum = sum + (temp%10) ** 3
#             temp = temp // 10  # 注意这里用地板除
#
#         if sum == each:
#             print(each, end='\t')
#
# print("所有的水仙花数分别是：", end='')
# Narcissus()
# def daff():

def Findstr(dststr,substr):
    count=0
    length=len(dststr)
    if substr not in dststr:
        print("未找到相应字符串！")
    else:
        for each in range(length-1):
            if dststr[each] == substr[0]:
                if dststr[each+1]==substr[1]:
                    count+=1
        print("子字符串在目标字符串中共出现 %d 次" % count)

dststr=input("请输入字符串：")
substr=input("请输入要检测的字符串：")
Findstr(dststr,substr)

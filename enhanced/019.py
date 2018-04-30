"""
019课程内容
1、函数与过程，函数都有返回值，有返回值就返回值，没有就返回none。
2、python可以有多个返回值。
3、函数变量的作用域问题：局部变量和全局变量。
4、尽量在写代码的时候，不要使用全局变量。
"""
# def palindrome(string):
#     length = len(string)#先得到这个字符串的长度
#     last = length-1#这样可以得到这个字符串的最后一位字符
#     length //= 2#不管是奇数还是偶数的字符个数，这样都是可以得到一半的值
#     flag = 1#标志位
#     for each in range(length):
#         if string[each] != string[last]:#判断第一位是否等于最后一个字符
#             flag = 0
#         last -= 1#往前走一步，倒数第二个字符和正数第二个字符再比较
#
#     if flag == 1:
#         return 1
#     else:
#         return 0
#
# string = input('请输入一句话：')
# if palindrome(string) == 1:
#     print('是回文联!')
# else:
#     print('不是回文联！')

# def palindrome(string):
#     """
#     一种简单有效判断回文联的方法，就是倒换过来，看看是不是还一样，这不就是回文联的特性吗？
#     有的时候，不一定从正面去攻克这个难题，可以从别的方法想问题。
#     :param string:
#     :return:
#     """
#     list1 = list(string)
#     list2 = reversed(list1)#reversed函数是倒换的功能
#     if list1 == list(list2):
#         return '是回文联!'
#     else:
#         return '不是回文联！'
# print(palindrome('上海自来水来自海上'))
def count(*param):
    """
    这里使用到了收集参数，因为你不知道你将输入几个参数，
    :param param:
    :return:
    """
    length = len(param)
    for i in range(length):
        letters = 0
        space = 0
        digit = 0
        others = 0
        for each in param[i]:
            if each.isalpha():
                letters += 1
            elif each.isdigit():
                digit += 1
            elif each == ' ':
                space += 1
            else:
                others += 1
        print('第 %d 个字符串共有：英文字母 %d 个，数字 %d 个，空格 %d 个，其他字符 %d 个。' % (i + 1, letters, digit, space, others))


count('I love fishc.com.', 'I love you, you love me.')

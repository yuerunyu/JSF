"""
021课程内容：
1、匿名函数lambda：
lambda x : x*2+1
前边是函数参数，后边是函数的内容
可以不用为函数命名头疼，在linux服务器上配置脚本比较容易
2、两个BIF
filter(function or none,iterable)过滤函数
map(function or none,iterable)映射函数:就是将可迭代对象当作参数进行函数运算，再生成一个可迭代对象结果。
"""
print(list(filter(lambda x : x%2,range(10))))
print(list(map(lambda x : x*2,range(10))))
print(list(filter(lambda n : not(n%3), range(1, 100))))
print(list(zip([1, 3, 5, 7, 9], [2, 4, 6, 8, 10])))
print(list(map(lambda x,y: [x,y],[1, 3, 5, 7, 9], [2, 4, 6, 8, 10])))
print(i for i in range(1, 100) if not(i%3))


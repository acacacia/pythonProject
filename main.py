# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import keyword
import sys
from random import shuffle


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
'''if __name__ == '__main__':
    print_hi('PyCharm')'''

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
'''for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}'.format(j, i, j*i), end=" ")
    print("")'''



print(r'\n')
i, c = 5, 3
a = i / c
a = str(a)[0:4]
print(a)
a = float(a)
print(type(a))

# 列表list 可变
l = [1, 2, 3, 4, 5, 6]
l[1] = 0
print(l[::-1])

# 元组tuple 不可变
t = (1, 2, 3, 4, 5, 6)
print(t[0:-2])
# 创建一个空元组
t = ()
# 如果元组中只存在一个元素要在元素后加"," 否则会认为tuple的type不是tuple 而是元组中唯一元素的type
t = (a,)
print(t)
print(type(t))

# 集合set 可变
# 可以用{}或set()创建集合 创建空集合必须用set()  {}是用来创建一个空字典
s1 = {1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 8}
s2 = {1, 2, 3, 4, 5, 6, 7}
# "-"差集  "|"并集  "&"交集  "^"两集合中不同时存在的元素  一个set中不能存在相同元素
print(s2 ^ s1)

# 字典dictionary 可变 (映射类型) key必须为不可变类型且不可重复 否则会被重新赋值
dict = {1: "name", "2": [1, 2, 3]}
print(dict)

str = 'hello'
print(repr(str))
print(str)

# list推导式
l[1] = 2
print(l)
l2 = [li for li in l if li % 2 == 0]
print(l2)
l3 = [i1 for i1 in range(10) if i1]
print(l3)

# dictionary推导式
# dic = {key: value for i2 in 集合(set、list、tuple)}
dic = {i2: i2 ** 3 for i2 in {1, 2, 3, 4}}
print(dic)

# tuple推导式 和list推导式用法相同 tuple推导式返回的是一个生成器对象 需要使用tuple()方法转换成tuple
t1 = (x for x in range(10))
print(t1)  # 结果: <generator object <genexpr> at 0x00000221AB7D8BA0>
print(tuple(t1))  # 结果: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

shuffle(l3)
print(l3)




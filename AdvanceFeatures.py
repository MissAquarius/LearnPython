# -*- coding:utf-8 -*

from collections import Iterable

'''
# 切片L[a,b] 表示从索引L[a]开始取，到索引L[b],不包括索引L[b]
L=list(range(100))
print(L[0:10])  #取前十个数
print(L[90:100])  #取后十个数
print(L[10:20])  #取前11-20十个数

print(L[0:10:2])  #取前十个数,每2个取一次
print(L[90:100:5])  #取后十个数,每5个取一次

print(L[:])  #复制L

# tuple也可以进行切片操作
t=("gexin")
print(t[0:2])
print("substring"[2:5]) #获取字符串的子串

# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法
def trim(s):
    if(s[0]==' ' and s[-1]==' '):
        return s[1:len(s)-1]
    else:
        if(s[0]==' ' and s[-1]!=' '):
            return s[1:len(s)]
        else:
            if (s[0] != ' ' and s[-1] == ' '):
                return s[0:len(s) - 1]
            else:
                return s

print(len(" hello "),len(trim(" hello ")),trim(" hello "))
print(len(" hello"),len(trim(" hello")),trim(" hello"))
print(len("hello "),len(trim("hello ")),trim("hello "))
print(trim(" hello world "))


# 迭代iteration
# 只要是可迭代对象，无论有无下标，都可以迭代，比如dict
dict={"gexin":90,"hmj":95,"hz":85}
for key in dict:
    print(key)   #迭代key，默认也是迭代key

for value in dict.values():
    print(value)  #迭代value

for key,value in dict.items():
    print(key,value)  # 同时迭代key和value

# 使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，不关心该对象究竟是list还是其他数据类型
# 使用collections模块的Iterable类型判断对象是否可迭代
print(isinstance(123,Iterable))
print(isinstance("123",Iterable))


# 请使用迭代查找一个list中最小和最大值，并返回一个tuple
def FindMinAndMax(L):
    if(L==[]):
        return ('None','None')
    else:
        Max=L[0]
        Min=L[0]
        for value in L:
            if value>Max:
                Max=value
            elif value<Min:
                Min=value
        return (Min,Max)

print(FindMinAndMax([]))
print(FindMinAndMax([7]))
print(FindMinAndMax([7,7]))
print(FindMinAndMax([7,1]))
print(FindMinAndMax([2,8,5,7]))

# 改进版本 接收的list包含非数字元素
def FindMinAndMax2(L):
    if(L==[]):
        return ("None","None")
    else:
        for value in L:
            if(isinstance(value,int)=="False"):
                break
                return ("error")
    Max = L[0]
    Min = L[0]
    for value in L:
        if value > Max:
            Max = value
        elif value < Min:
            Min = value
    return (Min, Max)



print(FindMinAndMax2([]))
print(FindMinAndMax2([7]))
print(FindMinAndMax2([7,7]))
print(FindMinAndMax2([7,1]))
print(FindMinAndMax2([1,2,8,'kkk']))
'''
L=[0,1,'abc']
for value in L:
    if isinstance(value,int)=="False":
        print(value)

print(isinstance('abc',int))
# -*- coding:utf-8 -*

from collections import Iterable
import os

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
    # 首先遍历list，排除包含非数字的元素
    for v in L:
        if (isinstance(v, int) == 0):
            return ("error")
    # list全为数字
    if(L==[]):
        return ("None","None")
    else:
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


# 是否可以遍历一次，就得到结果？
# 判断元素是否是int类型的时候，isinstance(v, int) == "False" 为什么不对？因为左边返回的是bool类型的，右边是字符串类型
if(isinstance('abc',int)==0):
    print("hahaha")
if (isinstance('abc', int) == bool("")):
    print("hahaha2")
else:
    print("hahaha3")

# 列表生成式 list Comprehensions

# 要生成1,2,3...10，如何做？
print(list(range(1,11)))
# 要生成1*1,2*2,3*3...10*10，如何做？
L=[]
for i in range(1,11):
    L.append(i*i)
print(L)
# 循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list
print([x*x for x in range(1,11)])
print([y*y for y in range(1,11) if y%2 == 0])
# 两层循环，可以生成全排列
print([m+n for m in "ABC" for n in "XYZ"])
# 列出当前目录下的所有文件和目录名
print([d for d in os.listdir(".")])
# 把一个list中所有的字符串变成小写
list2=["HELLO","WoRLD","Hello","PYTHOn"]
print([s.lower() for s in list2])


# 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错，因此对上面的字符串转小写进行改进


def ChangeStrToUpper(L):
    for l in L:
        if (isinstance(l,str))==0:
            return("Type Error!")
    return([s2.upper() for s2 in L])


print(ChangeStrToUpper(["hello", "worLd", "HEllo", "PYTHon"]))
print(ChangeStrToUpper(["I", "Will", "ALWAYS", 18, "years", "OLD"]))
print(ChangeStrToUpper(["I", "Will", "ALWAYS", "Eighteen", "years", "OLD"]))

# 生成器generator
# 一边循环一边计算，保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出错误
# 一般通过for循环来输出,用不到next方法
print([x*x for x in range(1,11)])
G=(y*y for y in range(1,11))
for g in G:
    print(g)

# 著名的斐波拉契数列（Fibonacci）1, 1, 2, 3, 5, 8, 13, 21, 34, 除第一个和第二个数外，任意一个数都可由前两个数相加得到：
def Fib(max):
    a = 1
    b = 1
    if max == 0:
        print ("no output!")
    elif max == 1:
        print(a)
    elif max == 2:
        print(a, b)
    else:
        print(a, b)
        n = 2
        while n < max:
            print("n=",n,"a=",a,"b=",b,"a+b=",a+b)
            a, b = b, a+b    # 注意这个地方有坑
            n += 1

Fib(6)
# 再想简化版本的，上面这个太复杂了
# 没错，我昨晚走在回去的路上就想到了简化版本，
# 但是今天都有课，下午开会不想弄，为什么晚上这个点来写呢？因为觉得心里很难过，写代码时间会过得比较快


def FibEasy(max):
    if max<= 0:
        print("please input a number that great than 0!")
    else:
        (a,b,n) = (0,1,0)
        while n < max:
            print(b)
            n+=1
            (a,b)=(b,a+b)

FibEasy(6)

#  将这个函数变成生成器
def FibEasy2(max):
    if max<= 0:
        print("please input a number that great than 0!")
    else:
        (a,b,n) = (0,1,0)
        while n < max:
            yield b   # 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
            n+=1
            (a,b)=(b,a+b)
FibEasy2(8)

# 生成器在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行

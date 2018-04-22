# *-* coding:utf-8 *-
from functools import reduce
# 高阶函数
## 变量可以指向函数
f=abs
print(f)
print(f(-10))
## 函数名也是变量
## abs=10
## print(abs)  # 输出10,实际不会这么写，此处只是为了说明函数名也是一个变量

# 既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
def Add(a,b,f):
    return f(a)+f(b)
print(Add(-1,3,abs))

# map/reduce
# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
# map()传入的第一个参数是f，函数对象本身,结果是一个Iterator惰性，通过list()函数让它把整个序列都计算出来并返回一个list。
L=[1,2,3,4,5,6]
def f(x):
    return x*x
print(list((map(f,L))))
# 数字转字符串
print(list(map(str,L)))

# reduce()把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
# 把序列[1, 3, 5]变换成整数135
def f2(x,y):
    return x*10+y
print(reduce(f2,[1, 3, 5]))

#map与reduce联合使用，完成str2int函数
dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2num(s):
    return dict[s]


def fn(x, y):
    return x * 10 + y


def str2int(s):
    return reduce(fn, list(map(str2num, s)))


print(str2int('21321'))

'''
把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
'''
# 假设用户输入的都是字母，不考虑其他字符
# 首先将字符串里的所有字符都转为小写，然后再将首字母大写
# 字符串函数 大写：s.upper()  小写：s.lower()
# 字符串首字母大写：s.capitalize() 每个单词的首字母大写:s.title 大小写互换：s.swapcase()


def normalize(name):
    return (name.lower()).capitalize()  #此例中与title()作用相同

print(list(map(normalize,['adam', 'LISA', 'barT'])))


#  Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(a,b):
    return a*b

print(reduce(prod,[3,5,7,9]))


#  利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
# 网上的思路：先忽略小数点，将整个字符串转换成整数，然后再利用小数点的位置，将整数还原成小数（不可行，py不支持，利用的是除以10的n次方

def str2float(s):
    if s.find('.') == -1:  # 整数
        return reduce(fn, map(str2num, s))
    else:  # 小数
        index = s.find('.')+1 # 小数点位置
        return (reduce(fn, map(str2num, s.replace('.', ''))))/pow(10, len(s)-index)


print(str2float('123.4567'))


# 我的想法：从小数点开始，把字符串截开，前面按照整数处理，后面按照小数处理，最后两部分加起来
def fn2(x,y):
    return x*0.1+y


# 自定义字符串反转函数

def strinverse(s):
    i = 0
    newstr = ''
    for i in range(len(s)-1):
        newstr += s[len(s)-1-i]
    return newstr


def str2float1(s):
    index = s.find('.')
    highstr = s[:index]
    lowstr = strinverse(s[index:])+'0'

    highnum = int(reduce(fn, map(str2num, highstr)))
    lownum = float(reduce(fn2, map(str2num, lowstr)))
    # 利用切片实现反转 lownum= float(reduce(fn2, map(str2num, s[-1:index:-1]+'0')))
    return highnum+lownum


print(str2float1('123.4567'))


# 知识点：
# 字符串切片（切片L[a,b] 表示从索引L[a]开始取，到索引L[b],不包括索引L[b]）
# 字符串末尾加一个字符 s+'a'即可
# 感觉自己是真的笨的很，想的也很麻烦，唉
# 字符串利用切片实现反转：
str00="python"
print(str00[-1:2:-1]) # noh

# filter(),过滤函数，接收一个函数和一个序列
# filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
# 过滤掉偶数


def is_odd(n):
    if n % 2 == 1:
        return 1
    else:
        return 0


print(list(filter(is_odd, [1, 2, 3, 4, 5, 6])))

# 去除字符串中的空格s.strip()过滤掉首尾空格


def is_empty(s):
    return s and s.strip()


print(list(filter(is_empty, ['', '  ', ' a ', 'a', 'b', None])))

# 生成回数


def is_huishu(n):
    s = str(n)
    if s == s[::-1]:  # 反转
        return 1
    else:
        return 0
    

print(list(filter(is_huishu, range(50))))


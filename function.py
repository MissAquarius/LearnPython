# -*- coding: utf-8 -*

# 求绝对值 abs()
# 求最值 max()
# 数据类型转换 int()

import math
'''
请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
ax2 + bx + c = 0的两个解。
'''
def quadratic (a, b, c):
   if(math.pow(b,2)-4*a*c > 0):
       x1 = (-b + (math.sqrt(math.pow(b, 2)-4*a*c))) / (2*a)
       x2 = (-b - (math.sqrt(math.pow(b, 2) - 4*a*c))) / (2*a)
       return (x1, x2)
   elif(math.pow(b,2)-4*a*c == 0):
       x = (-b + (math.sqrt(math.pow(b, 2) - 4*a*c)))/(2*a)
       return (x)
   else:
       pass

a = int(input("enter a: "))
b = int(input("enter b: "))
c = int(input("enter c: "))
print(quadratic(a, b, c))

# 位置参数
# 自定义个平方函数
def mypow(x):
    if not isinstance(x, (int, float)):
        raise TypeError("bad operate type")
    else:
        return (x*x)
print(mypow(2))

# 默认参数
# 改写自定义平方函数,默认是平方
def mypow2(x,n=2):
    if not isinstance(x, (int, float)):
        return TypeError('bad operate type')
    else:
        s=1
        while n>0:
           s*=x
           n-=1
        return s
print(mypow2(2))
print(mypow2(2, 3))


def student(name, sex, age=6, city='wuhan'):
    print(name, sex, age, city)

# 默认参数，按顺序给出
student("gexin", "女")
student("gexin", "女", 12)
# 默认参数，不按顺序给出
student("gexin", "女", city='beijing')

# Tips: 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。

# 默认参数的“坑”

def AddList(l=[]):
    l.append("love")
    return l
l=[]
print(AddList(['I', 'you']))  #['I', 'you', 'love']
print(AddList())  #['love']
print(AddList())  #['love', 'love']

# 默认参数必须指向不可变对象
def AddList2(l=None):
    if l==None:
        l=[]
        l.append("love")
    return l

print(AddList2())  # ['love']
print(AddList2())  # ['love']

# -*- coding: utf-8 *-

# 递归函数
def move(a, b, c, n):
    if n==1:
        print(a, "--", c)
    else:
        move(a, c, b, n-1)
        print(a, "--", c)
        move(b, a, c, n-1)

move('A', 'B', 'C',3)
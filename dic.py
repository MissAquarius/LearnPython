# -*- coding: utf-8 -*

# 成绩排名


"""
 输入每个人的姓名，成绩；输出从大到小排序之后的名字及成绩
"""


# 接收输入
n = input("Please Input The Number of The Total Students\n")
totalNum = int(n)
i = 0
l = []
while i < totalNum:
    d = {}
    name = input('name: ')
    score = input('score: ')
    d['name'] = name
    d['score'] = int(score)
    l.append(d)
    i += 1
print(l)
l.sort(key=lambda x: x['score'])
print(l)

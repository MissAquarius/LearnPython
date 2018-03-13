# -*- coding: utf-8 -*

# 计算1+2+...+100
sum = 0
for x in range(101):
    sum += x
print(sum)

sum = 0
n = 0
while n < 100:
    n+=1
    sum += n
print(sum)

# 计算1+3+5+...+99
sum = 0
for x in range(101):
    if x % 2 == 1:
        sum += x
print(sum)

sum = 0
n= 101
while n > 1:
   n=n-2
   sum+=n
print(sum)



# 计算2+4+6+...+100
sum = 0
for x in range(101):
    if x % 2 == 0:
        sum += x
print(sum)

n=0
sum=0
while n<99:
    n+=2
    sum+=n
print(sum)

newList = ['redis', 'python', 'c++']
i = 0
while i < len(newList):
     print('hello,', newList[i])
     i += 1

i=0
for i in range(10):
    if i % 2 == 0:
        continue
    else:
        if(i>5):
            break
        else:
            print(i)

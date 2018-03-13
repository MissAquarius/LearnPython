# -*- coding: utf-8 -*


#输入输出
name = input("Please Input You Name: ");
print("Your Name Is :", name);
print("1024*768=", 1024*768);

a = input('Please Input A Number');
a2=int(a);
if(a2>=0):
    print(a2);
else:
    print(-a2);


str="gexin";
str2=str;
print("str=", str, "str2=", str2);
str="gexin123";
print("str=", str, "str2=", str2);

# 数组
newStudent = ['gexin','gx'];
print(newStudent);
newStudent.append('xinxin');
print(newStudent);
newStudent.insert(0,'gege');
print(newStudent);
newStudent.pop();
print(newStudent);
newStudent.pop(0);
print(newStudent);

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0]);
# 打印Python:
print(L[1][1]);
# 打印Lisa:
print(L[2][2]);


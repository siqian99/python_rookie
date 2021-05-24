#1
import os
filename = open("Grade1.txt",'w')
from sys import argv

f1 = open("Score1.txt",'r')
for f2 in open("Score1.txt",'r'):
    f2 = f1.readline()
    f2 = f2.split(",")
    f2 = list(map(int, f2))
    a = sum(f2)
    print(a)
    if 0<= a < 100:
        f2 = open("Grade1.txt",'a')
        f2.write("E"+ "\n")
    elif 100 <= a < 200:
        f2 = open("Grade1.txt",'a')
        f2.write("D"+ "\n")
    elif 200 <= a < 300:
        f2 = open("Grade1.txt",'a')
        f2.write("C"+ "\n")
    elif 300 <= a < 400:
        f2 = open("Grade1.txt",'a')
        f2.write("B"+ "\n")
    else:
        f2 = open("Grade1.txt",'a')
        f2.write("A"+ "\n")

#2
import os
filename = open("Grade2.txt",'w')

f1 = open("Score1.txt",'r')
b = 0
c = 500
for f2 in open("Score1.txt",'r'):
    f2 = f1.readline()
    f2 = f2.split(",")

    f2 = list(map(int,f2))

    print(f2)
    a = sum(f2)

    print(a)
    while a>b:
        f2 = open("Grade2.txt",'w')
        f2 = f2.write(str(a)+"\n")
        b = a
    else:
        f2 = open("Grade2.txt",'w')
        f2 = f2.write(str(b)+"\n")
        b = b

    while a<c:
        f2 = open("Grade2.txt",'a')
        f2 = f2.write(str(a)+"\n")
        c = a
    else:
        f2 = open("Grade2.txt",'a')
        f2 = f2.write(str(c)+"\n")
        c = c
# 我不明白，这个为什么我只加入c的转义符号，不能换行，全加上才可以

#3
import os
filename = open("Grade3.txt",'w')
f1 = open("Score2.txt",'r')
for f2 in open("Score2.txt",'r'):
    f2 = f1.readline()
    f2 = f2.split()
    f2 = list(map(int,f2))
    a = f2[0]
    print(a)
    while a >= 60:
        f2 = open("Grade3.txt",'w')
        f2 = f2.write(str(a))
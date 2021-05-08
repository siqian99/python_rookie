#1
print("What is your name?")
name = input()
print("How old are you?",end=' ')
age = input()
# 可以在打印的末尾加一个 end = ' ', 打印后不换行
#2
a = int(input("数学 = "))
b = int(input("语文 = "))
c = int(input("英语 = "))
print("总分:",end='')
print(a+b+c)
#3
from sys import argv
Score = argv
f1 = open("Score.txt")
f2 = f1.readline()
f3 = f1.readline()
f4 = f1.readline()
a = int(f2)
b = int(f3)
c = int(f4)
print("总分:",end='')
print(a+b+c)
f1.close()
#4
from sys import argv
Score = argv
f1 = open("Score.txt",'a')
f1.write("238")
f1.close()
#5
from sys import argv
Chinese = argv
English = argv
Math = argv
f1 = open("Chinese.txt.TXT")
f2 = open("English.txt.TXT")
f3 = open("Math.txt.TXT")
F1 = f1.read()
F2 = f2.read()
F3 = f3.read()
a = int(F1)
b = int(F2)
c = int(F3)
F4 = str(a+b+c)
f4 = open("Total.TXT",'a')
f4.write(F4)


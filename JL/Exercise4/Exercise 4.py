#1
#(1)
var1 = "thisisquestionone"
var2 = var1[6:14]
print(var2)
#(2)
var1 = ["python","Link"]
var2 = ["",""]
var2[0], var2[1] = var1[1], var1[0]
print(var2)
#(3)
var1 = ["question","one"]
var1.append("two")
a = ["This","is"]
var2 = a +var1
print(var2)

#2
#(1) "abc" = "abc" 是赋值
print(False)
#(2)
a = [1,2]
b = [1,2]
if a==b:
    print(True)
#（3）
a = 0.1+0.2
b = 0.01*30
if a==b:
    print(True)
else:
    print(False)
#(4)
a = [1,2,3,4,5]
b = [1,2,3,4]
b.append(4)
b.append(5)
b.insert(0,0)
b = b[1:6]
if a==b:
    print(True)
else:
    print(False)
#(5)
a = 1+2
b = 10.5/3.5
if a==b:
    print(True)
else:
    print(False)

#3
from sys import argv
Score1 = argv
f1 = open("Score1.txt")
f2 = f1.readline()
s = 0
for f2 in open("Score1.txt",'r'):
    f2 = f2.split(",")
    f2 = list(map(float, f2))
    for i in f2:
        if i < 60:
            s = s+1
        else:
            s=s
print("Link有" + str(s) + "门课不及格")

#4
from sys import argv
Score1 = argv
f1 = open("Score2.txt")
f2 = f1.readline()
a = 0
for f2 in open("Score2.txt",'r'):
    f2 = f2.split(",")
    f2 = list(map(int, f2))
    for i in f2:
        a += i
b = [range(0,100),range(100,200), range(200,300),range(300,400),range(400,500)]
s = 0
F1 = [s]
for i in b:
    if a not in i:
        s = s+1
        F1.append(s)
    else:
        break
c = ["E","D","C","B","A"]
f7 = open("Grade.txt", 'w')
f7.write(c[F1[-1]])

#5
from sys import argv
GradeAll = argv
f1 = open("Score3.txt")
for f2 in open("Score3.txt",'r'):
    f2 = f1.readline()
    f2 = f2.split(",")
    f2[0] = f2[0][1:]
    f2[4] = f2[4][0:2]
    f2 = list(map(int, f2))
    a = sum(f2)
    f2 = open("GradeAll.txt", 'a')
    f2.write(str(a)+"\n")
    print(a)
#1
#1)
var1 = "thisisquestionone"
var2 = var1[6:14]
print(var2)
#2)
var3 = ["python", "Link"]
var4 = [var3[-1], var3[0]]
print(var4)
#3)
var5 = ["question", "one"]
var6 = ["This", "is", var5[0], "two"]
print(var6)

#2
#False
#True
#False
#False
#True

#3
score1 = open(r'C:\Users\lijia\Desktop\PyCharm\Test4\Score1.txt', 'r', encoding= "utf-8")
content = score1.read()
score1_s = content.split()
print(score1_s)
for i in score1_s:
    if float(i) < 60:
        print(i)
score1.close()

#4
score2 = open(r'C:\Users\lijia\Desktop\PyCharm\Test4\Score2.txt', 'r', encoding= "utf-8")
content2 = score2.read()
score2_s = content2.split()
print(score2_s)
total = 0
for j in score2_s:
    total += float(j)
print(total)
score2.close()

grade = open(r'C:\Users\lijia\Desktop\PyCharm\Test4\Grade.txt', 'w', encoding='utf-8')
if 400 <= total <= 500:
    grade.write('A')
elif 300 <= total < 400:
    grade.write('B')
elif 200 <= total < 300:
    grade.write('C')
elif 100 <= total < 200:
    grade.write('D')
else:
    grade.write('E')
grade.close()

#5
score3 = open(r'C:\Users\lijia\Desktop\PyCharm\Test4\Score3.txt', 'r', encoding= "utf-8")
content3 = score3.readlines()
score3_s1 = content3[0][1:-2].split(",")
score3_s2 = content3[1][1:-2].split(",")
score3_s3 = content3[-1][1:-1].split(",")
print(content3)
print(score3_s1)
print(score3_s2)
print(score3_s3)
sum1 = 0
sum2 = 0
sum3 = 0
for a in score3_s1:
    sum1 += float(a)
    if 400 <= sum1 <= 500:
        grade1 = 'A'
    elif 300 <= sum1 < 400:
        grade1 = 'B'
    elif 200 <= sum1 < 300:
        grade1 = 'C'
    elif 100 <= sum1 < 200:
        grade1 = 'D'
    else:
        grade1 = 'E'
print(grade1)

for b in score3_s2:
    sum2 += float(b)
    if 400 <= sum2 <= 500:
        grade2 = 'A'
    elif 300 <= sum2 < 400:
        grade2 = 'B'
    elif 200 <= sum2 < 300:
        grade2 = 'C'
    elif 100 <= sum2 < 200:
        grade2 = 'D'
    else:
        grade2 = 'E'
print(grade2)

for c in score3_s3:
    sum3 += float(c)
    if 400 <= sum3 <= 500:
        grade3 = 'A'
    elif 300 <= sum3 < 400:
        grade3 = 'B'
    elif 200 <= sum3 < 300:
        grade3 = 'C'
    elif 100 <= sum3 < 200:
        grade3 = 'D'
    else:
        grade3 = 'E'
print(grade3)

grade_all = open(r'C:\Users\lijia\Desktop\PyCharm\Test4\GradeAll.txt', 'w', encoding='utf-8')
grade_all.write("["+grade1+','+grade2+','+grade3+"]")
grade_all.close()


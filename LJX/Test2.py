#1
#在每一个打印行末尾加一个 end = ' '

#2
#Chinese = int(input('您的语文成绩是：'))
#Math = int(input('您的数学成绩是：'))
#English = int(input('您的英语成绩是：'))

#print(Chinese+Math+English)

#3
score = open(r'C:\Users\lijia\Desktop\PyCharm\Test2\Score.txt', 'r', encoding='utf-8')
content = score.read()
print(content)
score.close()

s = content.split()
total = 0
for i in s:
    total += int(i)
print(total)

#4
score2 = open(r'C:\Users\lijia\Desktop\PyCharm\Test2\Score2.txt', 'a', encoding='utf-8')
score2.write('\nTotal: '+str(total))
score2.close()

#5
score3 = open(r'C:\Users\lijia\Desktop\PyCharm\Test2\Total.txt', 'w', encoding='utf-8')
score3.write('Total: '+str(total))
score3.close()


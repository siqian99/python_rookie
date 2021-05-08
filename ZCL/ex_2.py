#1
#在打印行末尾放 end=''

#2
print("The score of language",end='')
language = input()
print("The score of math",end='')
math = input()
print("The score of english",end='')
english = input()

print(f"So, total score is ",end='')
print(int(language)+int(math)+int(english))

#3
a = open('Score.txt')
language_1 = a.readline()
math_1 = a.readline()
english_1 = a.readline()
print(int(language_1)+int(math_1)+int(english_1))
a.close()

#4
b = open('Score_1.txt',"r+")
language_2 = int(b.readline())
math_2 = int(b.readline())
english_2 = int(b.readline())
total = str(language_2+math_2+english_2)
b.write('\n')
b.write(total)
b.close()

#5
c = open('Chinese.txt',"r")
d = open('Math.txt',"r")
e = open('English.txt',"r")
f = open('Total.txt',"a")
language_3 = int(c.readline())
math_3 = int(d.readline())
english_3 = int(e.readline())
total_3 = str(language_3+math_3+english_3)
f.write(total_3)
c.close()
d.close()
e.close()
f.close()
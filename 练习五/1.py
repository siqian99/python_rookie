a = 666
list = []
while (a!=0):
    list.append(a % 2)
    a = a // 2
for i in range(0,len(list)):
    print(list[len(list)-i-1],end="")
a = 666
list = []
while (a!=0):
    list.append(a % 8)
    a = a // 8
for i in range(0,len(list)):
    print(list[len(list)-i-1],end="")

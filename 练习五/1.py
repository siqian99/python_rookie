f1 = open("Score2.txt", 'r')
f2 = f1.readline()
while (f2 != None):
    if (f2 >= "60"):
        f3 = open("Grade3.txt", 'w')
        f3.write(f2)
        exit(0)
    f2 = f1.readline()

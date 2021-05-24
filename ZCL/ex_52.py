#1
f = open('Grade2.txt', "a")
Score = open('Score1.txt',"r")

g=0
ll = Score.readline()
while l!="":
    l = ll.split(",")
    #print(l)
    eee = l[4][0:2]
    e = int(eee)
    if g <= e:
        g=e
    else:
        g=g
    ll = Score.readline()
    print(ll)

f.write(str(g))
f.close()
Score.close()
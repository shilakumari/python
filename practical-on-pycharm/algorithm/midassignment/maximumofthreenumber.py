a,b,c = 11,3,17
l=[]
l.append(a)
l.append(b)
l.append(c)
#l.sort()
#print(l[-1])
maximum = -1
for i in l:
    if maximum<i:
        maximum = i
print(maximum)



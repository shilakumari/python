n=5
gas=[1,2,3,4,5]
cost=[3,4,5,1,2]

ti=-1
flag=False
for i in range(n):
    ti=i
    g = gas[ti]
    for j in range(n):
        if g < cost[ti]:
            break
        g = g - cost[ti]
        if ti==(n-1):
            ti=0
        else:
            ti += 1
        if j==(n-1) and g >= 0:
            ti=i
            flag=True
            break
        g = g + gas[ti]
    if flag:
        break

if flag:
    print("ti", ti)
else:
    print(-1)
